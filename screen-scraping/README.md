
Text Scraper
========

Download texts from lib.ru and az.lib.ru. Useful for selecting a set of texts and automatically running them.

Process:
------

Create a file with authors and links to texts. Use the following format

To specify downloading all works an author has written, use this:
```
{Author name (can contain spaces and punctuation)} {URL of author page(beginning with 'http' or 'https'}
```

To specify only certain sections, include them with "Section: ..." below the name. The section titles
can be a comma-separated list, or a range (from X to Y). To start from the beginning of the page, write
`Sections: from the beginning to {actual section name}`.

Example:
```
Dostoevsky, Fyodor http://az.lib.ru/dostoevsky-f/
Sections: from the beginning to Prose
```

Then, run `python downloader.py {your filename}`. The output will be an SQLite database with the full
text of each work as a complete file.

Requirements:
----

This uses selenium and Firefox. Other browsers can be implemented by changing the code, but Chrome
is rather difficult to configure.


Other sites:
-----

This program is designed to work with az.lib.ru texts primarily. To add parsers for other sites,
create new classes modeled on the classes in `extract_author_links.py`. 

