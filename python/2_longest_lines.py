# pylint: disable=invalid-name, missing-docstring

from __future__ import print_function

import sys

with open(sys.argv[1], 'r') as fh:
    lines = fh.readlines()
    count = int(lines[0])
    sentences = sorted(lines[1:], key = lambda s: len(s), reverse = True)

    for i in range(count):
        print(sentences[i].strip())

