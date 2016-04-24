# pylint: disable=invalid-name, missing-docstring

from __future__ import print_function

import sys

NUMBER_WORDS = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
]

with open(sys.argv[1], 'r') as fh:
    for line in fh.readlines():
        line = line.strip()
        if line == '':
            continue

        numbers = line.split(';')
        print(''.join([str(NUMBER_WORDS.index(n)) for n in numbers]))

