# pylint: disable=invalid-name, missing-docstring

import sys

def sum_string(string, base):
    string = string.strip()

    return sum(
        int(comp, base)
        for comp in string.split(' ')
    )

with open(sys.argv[1], 'r') as fh:
    for line in fh.readlines():
        line = line.strip()
        if line == '':
            continue

        hex_component, bin_component = line.split('|')

        print(sum_string(hex_component, 16) <= sum_string(bin_component, 2))

