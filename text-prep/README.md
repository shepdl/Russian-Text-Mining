MALLET Russian Text Preparation Utilites
===


With these scripts, you will be able to start with a set of texts in HTML or plain-text format
and convert these into a set of files to import into MALLET.



This has the following components:

Removing proper names
-----

`proper_name_filter.py` contains a function for removing proper names. This scans a document 
and searches for any words with a capital letter, except for those that occur at the beginning
of a sentence. This is a fairly simple algorithm but it's proven to be very effective for us.


Converting RTF files to plain text
-----

`convert_rtf_to_txt.py [in_directory] [out_directory]`
Recursively convert all files in the contained folder from RTF files to text files. Uses Pyth.


Stopwords
-----

This also includes a useful list of Russian stopwords that includes many archaic terms
often found in earlier works of literature.

