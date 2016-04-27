# pylint: disable=invalid-name, missing-docstring

from __future__ import print_function

import sys

with open(sys.argv[1], 'r') as fh:
    for line in fh:
        numbers, indices = line.split(':')
        numbers = numbers.strip().split(' ')
        indices = [i.strip().split('-') for i in indices.strip().split(',')]

        for first, second in indices:
            first, second = int(first), int(second)
            numbers[first], numbers[second] = numbers[second], numbers[first]

        print(' '.join(numbers))

