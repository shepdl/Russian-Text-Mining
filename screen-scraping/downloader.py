# coding=utf8
__author__ = 'Dave Shepard'

import sys
import datetime
import codecs

import author_file_parsers
import extract_author_links
import LinkStore



def download_links(in_filename):
    attempt_filename = in_filename.replace('../', '').replace('.txt', '') + str(datetime.datetime.now()).replace(':', '-')\
        .replace('.', '-').replace(' ', '-') + '.db'
    in_file = codecs.open(in_filename, encoding='utf8')
    store = LinkStore.LinkStore(attempt_filename)

    parser = author_file_parsers.RootParser()
    author_link_extractor = extract_author_links.AuthorLinkExtractor()

    for raw_line in in_file:
        line = raw_line.strip()
        parser = parser.handle_line(line, author_link_extractor, store)

    author_link_extractor.close()
    print "Done"


if __name__ == '__main__':
    download_links(sys.argv[1])

