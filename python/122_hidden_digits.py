# pylint: disable=invalid-name, missing-docstring

from __future__ import print_function

import re
import sys

with open(sys.argv[1], 'r') as fh:
    for line in fh:
        line = re.sub(r'([^a-j0-9])', '', line.strip())

        if not line:
            print('NONE')
        else:
            output = ''
            for c in line:
                if c >= 'a' and c <= 'j':
                    output += str(ord(c) - ord('a'))
                else:
                    output += c
            print(output)

