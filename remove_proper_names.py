import codecs
import sys
import glob

from proper_name_filter import remove_proper_names_from_file

sys.stdout.write(remove_proper_names_from_file(sys.stdin))

