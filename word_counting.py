#!/usr/bin/python

import sys
import re
from string import punctuation
from operator import itemgetter

N = 1000
words = {}

with open(sys.argv[1]) as file: 
	text = file.read()
	words_gen = re.split('\W+', text.lower())

easy_words_gen = (word.strip(punctuation).lower() for line in open("easy_words.txt")
                                         for word in line.split())
for word in words_gen:
    words[word] = words.get(word, 0) + 1

for word in easy_words_gen:
	if word in words:
		del words[word]

top_words = sorted(words.items(), key=itemgetter(1), reverse=True)

for word, frequency in top_words:
    print ("%d\t\t%s" % (frequency, word))

