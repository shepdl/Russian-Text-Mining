#!/usr/bin/python
import sys
import os
import codecs

from BeautifulSoup import BeautifulSoup


out_file = sys.stdout

with open(sys.stdin) as in_file:
    in_file_contents = in_file.read() 
    in_html = BeautifulSoup(in_file_contents)

    for chapter in in_html.findAll('div', 'chapter'):
        for line_node in chapter.findAll('p'):
            out_file.write(line_node.text)
            out_file.write('\n')
            out_file.write('|')

