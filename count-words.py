#!/usr/bin/env python3

# get-platform-name: print short name of operating system/platform
# Copyright (C) 2018  "Michael G. Morey" <mgmorey@gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
