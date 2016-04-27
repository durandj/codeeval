# pylint: disable=invalid-name, missing-docstring

from __future__ import print_function

import re
import sys

NUMBERS_REGEX = re.compile(r'(\d+)')
WORDS_REGEX = re.compile(r'([a-z]+)', re.I)

with open(sys.argv[1], 'r') as fh:
    for line in fh:
        tokens = line.strip().split(',')
        words = [w for w in tokens if WORDS_REGEX.match(w)]
        numbers = [n for n in tokens if NUMBERS_REGEX.match(n)]

        if len(words) and len(numbers):
            print('|'.join((','.join(words), ','.join(numbers))))
        elif len(words):
            print(','.join(words))
        else:
            print(','.join(numbers))

