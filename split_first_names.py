#! /usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import re

def delete_stress_marks(string):
    stress_mark = u'\u0301'
    result = u''
    for symbol in string:
        if symbol != stress_mark:
            result += symbol
    return result

def clean_words(string):
    result = u''
    expr = re.compile(ur'(\w{2,})[ ,)\n]', re.UNICODE)
    m = re.findall(expr, string)
    result = ' '.join(m)
    return result

f = codecs.open("list_of_first_names.txt", "r", "utf-8")
name = f.read()
f.close()
name = delete_stress_marks(name)
name = clean_words(name)
w = codecs.open('names.txt', "w", "utf-8")
w.write(name)
w.close()
