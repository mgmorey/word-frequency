#!/usr/bin/env python3

import string

counts = {}
filename = 'metamorphosis.txt' 
table = str.maketrans('', '', string.punctuation)

with open(filename, 'rt') as f:
    text = f.read()

words = [w for w in text.split() if w.isalpha()]
stripped_words = [w.translate(table) for w in words]
lower_stripped_words = [w.lower() for w in stripped_words]

for word in lower_stripped_words:
    counts[word] = counts[word] + 1 if word in counts else 1

for pair in sorted(((v, k) for k, v in counts.items()), reverse=True):
    print('{:30s} {:5d}'.format(pair[1], pair[0]))
