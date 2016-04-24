# pylint: disable=invalid-name, missing-docstring, redefined-outer-name

from __future__ import print_function

import sys

def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield (i, number // i)

with open(sys.argv[1], 'r') as fh:
    for line in fh.readlines():
        line = line.strip()
        if line == '':
            continue

        for period, count in factorize(len(line)):
            if line[:period] * count == line:
                print(period)
                break

