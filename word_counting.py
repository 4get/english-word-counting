import sys
from string import punctuation
from operator import itemgetter

N = 100
words = {}

for filename in sys.argv[1:]:  
	words_gen = (word.strip(punctuation).lower() for line in open(filename)
                                         for word in line.split())

for word in words_gen:
    words[word] = words.get(word, 0) + 1

top_words = sorted(words.items(), key=itemgetter(1), reverse=True)[:N]

for word, frequency in top_words:
    print ("%s %d" % (word, frequency))

