import codecs
import sys
import glob

from proper_name_filter import remove_proper_names_from_file

for in_filename in glob.glob('../dostoevsky/*.txt'):
    # in_filename = sys.argv[1]
    # out_filename = sys.argv[2]

    chapter_number = in_filename.split('/')[-1].split('.')[0]
    out_filename = 'proper-name-test/{}.txt'.format(chapter_number)

    with codecs.open(in_filename, encoding='utf-8') as in_file, codecs.open(
            out_filename, 'w', encoding='utf-8'
            ) as out_file:

        for line in remove_proper_names_from_file(in_file):
            out_file.write(line)

        # for line in in_file:
        #     out_file.write(remove_proper_names(line))
            
