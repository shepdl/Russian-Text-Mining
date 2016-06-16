# coding=utf8
__author__ = 'Dave Shepard'

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class AuthorLinkExtractor(object):

    def __init__(self):
        self.browser = webdriver.Firefox()


    def get_links_from_individual_sections(self, author_link, sections):
        parser = ParseSectionList(sections)
        work_links = []

        self.browser.get(author_link)
        try:
            works_container = self.browser.find_element_by_xpath('.//body/dd/dl')
        except NoSuchElementException:
            works_container = self.browser.find_element_by_xpath('.//body/dl')
        for link in works_container.find_elements_by_xpath('*'):
            parser = parser.handle_element(link, work_links)
            if parser is None:
                break

        return self.download_files(work_links)

    delete_header_script = """
        document.querySelectorAll('body > center')[0].remove();
    """

    def download_files(self, work_links):
        work_and_text = []
        for title, pub_year, url in work_links:
            self.browser.get(url)
            self.browser.execute_script(self.delete_header_script)
            work_container = self.browser.find_element_by_css_selector('body')
            work_and_text.append(
                [title, pub_year, url, work_container.text,]
            )
        print "Downloaded all texts"
        return work_and_text


    def get_links_from_section_range(self, author_link, sections):
        from_section = sections['from_section']
        to_section = sections['to_section']
        parser = ParseRange(from_section, to_section)
        work_links = []

        self.browser.get(author_link)
        try:
            works_container = self.browser.find_element_by_xpath('.//body/dd/dl')
        except NoSuchElementException:
            try:
                works_container = self.browser.find_element_by_xpath('.//body/dl')
            except NoSuchElementException:
                works_container = self.browser.find_element_by_xpath('.//body/li/dl')

        for link in works_container.find_elements_by_xpath('*'):
            if parser is None:
                break
            parser = parser.handle_element(link, work_links)


        return self.download_files(work_links)


    def close(self):
        self.browser.quit()


class ParseRange(object):

    def __init__(self, from_section_name, until_section_name):
        self.from_section_name = from_section_name
        self.until_section_name = until_section_name
        self.parsing = False

    def handle_element(self, link, work_links):
        if link.tag_name == 'p':
            link_text = link.text.strip()[0:-1]
            if link_text == self.until_section_name:
                return None
            if link_text == self.from_section_name or u'beginning' in self.from_section_name or self.parsing:
                self.parsing = True
                return ParseValidSection(self)
            if link_text != self.until_section_name:
                return ParseValidSection(self)
            return self
        else:
            return self



class ParseSectionList(object):

    def __init__(self, valid_section_list):
        self.valid_section_list = valid_section_list
        self.found_sections = []

    def handle_element(self, link, work_links):
        if link.tag_name == u'p':
            if len(self.found_sections) == len(self.valid_section_list):
                print u"Completed {}".format(', '.join(self.valid_section_list))
                return None
            link_text = link.text.split(':')[0].strip()
            if link_text in self.valid_section_list:
                self.found_sections.append(link_text)
                return ParseValidSection(self)
            else:
                return self
        elif link.tag_name == 'dl':
            # skip sections we aren't interested in
            return self
        else:
            return self



class ParseValidSection(object):

    def __init__(self, parent):
        self.parent = parent


    def handle_element(self, link, work_links):
        if link.tag_name == u'dl':
            link_element = link.find_elements_by_xpath('.//a[@href]')[0]
            title_element = link.find_elements_by_xpath('.//a[@href]/b')[0]
            if title_element.text.strip() == u'New':
                title_element = link.find_elements_by_xpath('.//a[@href]')[1]
            pub_year = link.find_elements_by_xpath('.//small')[0].text[1:-1]
            print u"Found {}, published in {}".format(title_element.text, pub_year)
            url = link_element.get_attribute('href')
            work_links.append(
                (title_element.text, pub_year, url, )
            )
            return self
        elif link.tag_name == u'p' or link.tag_name[0] == u'h': # tag is <p> or <h[1-x]>
            return self.parent.handle_element(link, work_links)
        else:
            # Ignore other elements
            return self
