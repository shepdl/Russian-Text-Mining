import codecs
import glob
import re


stopword_list = [
    word for word in codecs.open('RussianStopWords.txt', encoding='utf-8').read().split(' ')
]

STEMMED_PATTERN = r'\{[\w|]+\}'

out_file = sys.stdout


for line in in_file:
    for word in re.findall(STEMMED_PATTERN, line, re.UNICODE):
        real_words = [w for w in word[1:-1].split('|') if w not in stopword_list]
        out_file.write(u' {}'.format('|'.join(real_words)))

