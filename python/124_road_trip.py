# pylint: disable=invalid-name, missing-docstring

from __future__ import print_function

import sys

with open(sys.argv[1], 'r') as fh:
    for line in fh:
        cities = sorted([
            int(token.rsplit(',')[-1])
            for token in line.strip().split(';')
            if token.strip()
        ])

        start = 0
        destinations = []
        for city in cities:
            destinations.append(str(city - start))
            start = city

        print(','.join(destinations))

