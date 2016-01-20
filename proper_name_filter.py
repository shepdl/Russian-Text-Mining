# coding=utf-8
import re


# PROPER_NAMES_PATTERN=u'[^.] [АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ]\\w+'
PROPER_NAMES_PATTERN=u'[^.] (?=([\u0410-\u042F][\u0430-\u044F]+))'

def remove_proper_names(in_string):
    matches = [m.group(1) for m in re.finditer(PROPER_NAMES_PATTERN, in_string, re.UNICODE)]
    for match in matches:
        in_string = in_string.replace(match, '')
    return in_string


def remove_proper_names_from_file(in_file):
    matches = set()
    for line in in_file:
        matches = matches.union(find_matches(line))
    in_file.seek(0)

    out_lines = []
    for line in in_file:
        current_line = line
        for match in matches:
            current_line = current_line.replace(match, '')
        out_lines.append(current_line)
    return out_lines


def find_matches(in_string):
    return set([m.group(1) for m in re.finditer(PROPER_NAMES_PATTERN, in_string, re.UNICODE)])
