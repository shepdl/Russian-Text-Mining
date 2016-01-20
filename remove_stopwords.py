import codecs
import glob
import re


stopword_list = [
    word for word in codecs.open('RussianStopWords.txt', encoding='utf-8').read().split(' ')
]


STEMMED_PATTERN = r'\{[\w|]+\}'

for in_filename in glob.glob('code/stemmed-texts/*.txt'):
    with codecs.open(in_filename, encoding='utf-8') as in_file:
        out_filename = 'dostoevsky-stopwords-removed/{}'.format(in_filename.split('/')[-1])
        with codecs.open(out_filename, 'w', encoding='utf-8') as out_file:
            for line in in_file:
                for word in re.findall(STEMMED_PATTERN, line, re.UNICODE):
                    real_words = [w for w in word[1:-1].split('|') if w not in stopword_list]
                    out_file.write(u' {}'.format('|'.join(real_words)))

