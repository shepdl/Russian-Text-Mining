# coding=utf8
import urllib

__author__ = 'Dave Shepard'

import re


class RootParser(object):

    def handle_line(self, line, work_list_page_browser, store):
        print u"RP handling {}".format(line)
        if AuthorParser.TRIGGER_PATTERN.match(line):
            author_info = AuthorParser.TRIGGER_PATTERN.match(line).groupdict()
            return AuthorParser(self, author_info['author'], author_info['url'])
        elif AuthorWithSingleWorksParser.TRIGGER_PATTERN.match(line):
            author_info = AuthorWithSingleWorksParser.TRIGGER_PATTERN.match(line).groupdict()
            return AuthorWithSingleWorksParser(self, author_info['author'])
        else:
            return self


class AuthorWithSingleWorksParser(object):

    TRIGGER_PATTERN = re.compile(ur'^(?P<author>[A-Za-z]+, [.]+)', re.UNICODE)

    WORK_LINE = re.compile(ur'^(?P<url>http://[\S]+) Date: (?P<date>[\d]+)', re.UNICODE)

    def __init__(self, parent_parser, author):
        self.parent_parser = parent_parser
        self.author = author

    def handle_line(self, line, work_downloader, store):
        if line.strip() == '':
            return self.parent_parser

        data = self.WORK_LINE.match(line)
        if data:
            store.insert_link(
                author=self.author,
                work=data['url'],
                pub_year=data['date'],
                url=data['url'],
                raw_text=urllib.urlopen(data['url']).read()
            )
            return self
        else:
            raise Exception(u"Unexpected line encountered: {}".format(line))



class AuthorParser(object):

    TRIGGER_PATTERN = re.compile(ur'^(?P<author>.*) (?P<url>(http://.*))$', re.UNICODE)

    FROM_TO_PATTERN = re.compile(ur'from (?P<from_section>.*) to (?P<to_section>.*)$', re.UNICODE)


    def __init__(self, parent_parser, author, author_page_url):
        self.parent_parser = parent_parser
        self.author = author
        self.author_page_url = author_page_url

    def handle_line(self, line, work_list_page_browser, store):
        print u"AP handling {}".format(line)

        if line.strip() == '':
            store.insert_link(author=self.author, url=self.author_page_url)
            return self.parent_parser
        elif line[0:3] == 'and':
            store.insert_link(author=self.author, url=self.author_page_url)
            url = line.split('and ')[1]
            store.insert_link(author=self.author, url=url)
        elif line[0] == '#':
            return self.parent_parser
        elif line[0:4] == 'http':
            store.insert_link(author=self.author, url=line)
            return self

        else:
            sections = None
            page_parser = None

            if 'Section:' in line:
                sections = [line.replace('Section:', '').strip(),]
                page_parser = work_list_page_browser.get_links_from_individual_sections
            elif 'Sections:' in line:
                if ' and ' in line:
                    sections = line.split(' and ')
                    page_parser = work_list_page_browser.get_links_from_individual_sections
                elif ',' in line:
                    sections = [s.strip() for s in line.split(',')]
                    page_parser = work_list_page_browser.get_links_from_individual_sections
                elif self.FROM_TO_PATTERN.search(line):
                    sections = self.FROM_TO_PATTERN.search(line).groupdict()
                    page_parser = work_list_page_browser.get_links_from_section_range
                else:
                    print line
                    raise Exception("Unexpected line encountered in AuthorParser")
            else:
                print "What happened?"

            for work, pub_year, link, text in page_parser(self.author_page_url, sections):
                store.insert_link(author=self.author, work=work, pub_year=pub_year, url=link, raw_text=text)

            return self.parent_parser
