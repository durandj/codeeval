# pylint: disable=invalid-name, missing-docstring

from __future__ import print_function

import sys

with open(sys.argv[1], 'r') as fh:
    for line in fh:
        number = int(line.strip())

        print(list(bin(number)).count('1'))

