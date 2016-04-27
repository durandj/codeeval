# pylint: disable=invalid-name, missing-docstring

from __future__ import print_function

import re
import sys

with open(sys.argv[1], 'r') as fh:
    for line in fh:
        sentence, pattern = tuple(line.split(','))
        pattern = '([{}])'.format(pattern.strip())

        print(re.sub(pattern, '', sentence))

