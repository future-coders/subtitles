#! /usr/bin/env python

import re
import collections

# https://en.wikipedia.org/wiki/SubRip
# http://stackoverflow.com/a/8010133
# http://stackoverflow.com/a/5552623

word_frequencies = collections.defaultdict(int)

with open('./pulp_fiction.srt', 'r', encoding="latin1") as file:
    
    for line in file:
        line = line.rstrip('\n')

        if re.search(r"^\s*$", line) \
        or re.search(r"^[0-9]+$", line) \
        or re.search(r"^[0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3} --> [0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3}$", line):
            continue
                
        if re.search(r"^- ", line):
            line = line.lstrip("- ")

        # print(line)
    	
        words = re.split(r"[\s\.\,\?\¿\!\"]+", line)
        words = filter(None, words)
        
        # print(words)

        for word in words:
            word = word.lower()

            word_frequencies[word] += 1

# print(word_frequencies)

words_sorted_by_frequency = sorted(word_frequencies, key=word_frequencies.get, reverse=True)

for word in words_sorted_by_frequency:
    print(word + " " + str(word_frequencies[word]))
