# pylint: disable=invalid-name, missing-docstring

from __future__ import print_function

import sys

with open(sys.argv[1]) as fh:
    for line in fh:
        words = line.strip().split(' ')
        words = sorted(words, key = lambda w: len(w), reverse = True)

        print(words[0])

