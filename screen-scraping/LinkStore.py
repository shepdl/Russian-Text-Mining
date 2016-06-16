# coding=utf8
__author__ = 'dave'

import sqlite3


class LinkStore(object):

    def __init__(self, filename):
        self.filename = filename
        self.db = sqlite3.connect(filename)

        self.db.execute('''
            CREATE TABLE IF NOT EXISTS works (
                id INTEGER PRIMARY KEY,
                author TEXT,
                publication_year INT,
                title TEXT,
                url TEXT,
                raw_text TEXT,
                cleaned_text
            )
        ''')

        self.cursor = self.db.cursor()
        self.insert_count = 0

    def insert_link(self, author=None, work=None, pub_year=None, url=None, raw_text=None):
        if author is None:
            author = ''
        if work is None:
            work = ''
        if pub_year is None:
            pub_year = None
        if url is None:
            url = ''
        if raw_text is None:
            raw_text = ''

        self.cursor.execute(
            '''INSERT INTO works (author, publication_year, title, url, raw_text) VALUES (?,?,?,?,?)''',
            (author, pub_year, work, url, raw_text,)
        )

        self.insert_count += 1

        if self.insert_count >= 10:
            self.insert_count = 0
            self.db.commit()

    def close(self):
        self.cursor.close()
        self.db.commit()
