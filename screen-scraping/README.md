
Screen Scraping
========

Download texts from lib.ru and az.lib.ru. Useful for selecting a set of texts and automatically running them.

Process
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

To include a single work, just put it after the author name. Place additional works on the following lines:
```
Dostoevsky, Fyodor http://az.lib.ru/dostoevsky-f/crime-and-punishment.html
http://az.lib.ru/dostoevsky-f/demons.html
```

The program will try to guess dates and work names from the listings on the author pages. To specify dates for
individual works, put "Date: " and the date after the text. For example:
```
Dostoevsky, Fyodor http://az.lib.ru/dostoevsky-f/crime-and-punishment.html Date: 1866
http://az.lib.ru/dostoevsky-f/demons.html Date: 1871
```

To comment out a line, put a '#' before it:

```
# The parser will skip this line
```


Running
----

Once your file is complete, run `python downloader.py {your filename}`. The output will be an SQLite database with the full
text of each work as a complete file.


Requirements
----

Selenium (included in the virtualenv requirements.txt) and Firefox. 


Extending
-----

This program is designed to work with az.lib.ru texts primarily. To add parsers for other sites,
create new classes modeled on the classes in `extract_author_links.py`. 


