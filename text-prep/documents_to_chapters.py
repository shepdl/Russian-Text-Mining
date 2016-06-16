#!/usr/bin/python
import sys
import os
import codecs

from bs4 import BeautifulSoup


def extract_chapters(in_filename):
    with codecs.open(in_filename, encoding='utf-8') as in_file:
        in_file_contents = in_file.read() 
        in_html = BeautifulSoup(in_file_contents, 'html.parser')

        out_buffer = []
        for line_node in in_html.findAll('p'):
            out_buffer.append(line_node.text)

        for line_node in in_html.findAll('span'):
            out_buffer.append(line_node.text)

        return out_buffer
