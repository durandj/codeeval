# pylint: disable=invalid-name, missing-docstring

from __future__ import print_function

import sys

with open(sys.argv[1], 'r') as fh:
    for line in fh.readlines():
        line = line.strip()
        if line == '':
            continue

        numbers = [int(n) for n in line.split(' ')]
        number_set = set(numbers)

        unique = [n for n in number_set if numbers.count(n) == 1]

        if len(unique) > 0:
            lowest = min(unique)

            print(numbers.index(lowest) + 1)
        else:
            print(0)

