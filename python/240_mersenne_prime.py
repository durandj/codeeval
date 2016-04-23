# pylint: disable=invalid-name, missing-docstring

import math
import sys

def is_prime(value):
    if value <= 1:
        return False
    elif value == 2:
        return True
    elif value % 2 == 0:
        return False

    root = math.sqrt(value)
    i = 3
    while i <= root:
        if value % i == 0:
            return False

        i += 2

    return True

def mersenne_primes(max_exponent):
    if max_exponent >= 2:
        yield 3

    exponent = 3

    while exponent <= max_exponent:
        if is_prime(exponent):
            yield int(math.pow(2, exponent) - 1)

        exponent += 1

with open(sys.argv[1], 'r') as fh:
    for line in fh.readlines():
        line = line.strip()
        if line == '':
            continue

        max_value = math.floor(math.log2(int(line)))
        print(
            ', '.join(str(p) for p in mersenne_primes(max_value))
        )

