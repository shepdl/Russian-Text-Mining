import glob
import codecs
import sys

from pyth.plugins.rtf15.reader import Rtf15Reader
from pyth.plugins.plaintext.writer import PlaintextWriter

in_dir, out_dir = sys.argv[1:3]

for in_filename in glob.glob('{}/*.rtf'.format(in_dir)):
    in_file = codecs.open(in_filename)
    out_filename = in_filename.split('/')[1].rsplit('.', 1)[0]
    out_file = codecs.open('{}/{}.txt'.format(out_dir, out_filename), 'w')
    doc = Rtf15Reader.read(in_file)

    PlaintextWriter.write(doc, out_file)

    in_file.close()
    out_file.close()
