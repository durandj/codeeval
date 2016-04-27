# pylint: disable=invalid-name, missing-docstring

from __future__ import print_function

import collections
import sys

with open(sys.argv[1], 'r') as fh:
    for line in fh:
        line = line.strip()

        count = collections.OrderedDict()
        for c in line:
            if c not in count:
                count[c] = 0

            count[c] += 1

        for c, n in count.items():
            if n == 1:
                print(c)
                break

