#!/usr/bin/python
import sys
import os
import codecs

from BeautifulSoup import BeautifulSoup


def scan_folder(directory, extension):
    for path, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith(extension):
                yield os.path.join(path, f)


in_dir = sys.argv[1]
out_dir = sys.argv[2]

try:
    os.makedirs(out_dir)
except OSError as ex:
    pass

for in_file_path in scan_folder(in_dir, '.htm'):
    containing_dir_path = in_file_path.replace('../', '')
    containing_directory = os.path.join(out_dir, os.path.splitext(containing_dir_path)[0])

    with open(in_file_path) as in_file:
        # Fix character encoding
        in_file_contents = in_file.read() 
        in_html = BeautifulSoup(in_file_contents)

        chapter_counter = 0
        
        for chapter in in_html.findAll('div', 'chapter'):
            # Don't create directory if there are no compatible files in it
            try:
                os.makedirs(containing_directory)
            except OSError as ex:  
                # Do nothing if the directory already exists
                pass
            with codecs.open('{}/{}.txt'.format(containing_directory, chapter_counter), 'w', encoding='utf-8') as out_file:
                for line_node in chapter.findAll('p'):
                    out_file.write(line_node.text)
                    out_file.write('\n')
            chapter_counter += 1

        if chapter_counter > 0:
            print containing_directory
            print "Found {} chapters".format(chapter_counter)


