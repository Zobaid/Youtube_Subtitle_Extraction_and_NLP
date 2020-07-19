# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 22:17:07 2020

@author: Ultimate-SK
"""

import re
bad_words = ['-->']


with open('song.vtt') as oldfile, open('newfile.txt', 'w') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)


with open('newfile.txt') as result:
    uniqlines = set(result.readlines())
    with open('sub_out.txt', 'w') as rmdup:
        mylst = map(lambda each: each.strip("&gt;&gt;"), uniqlines)
        print(mylst)
        rmdup.writelines(set(mylst))