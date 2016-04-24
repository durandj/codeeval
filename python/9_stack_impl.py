# pylint: disable=invalid-name, missing-docstring

from __future__ import print_function

import sys

class Stack(object):
    def __init__(self):
        self._stack = []
        self._size = 0

    def push(self, obj):
        self._stack.append(obj)
        self._size += 1

    def pop(self):
        self._size -= 1
        return self._stack.pop()

    def size(self):
        return self._size

with open(sys.argv[1], 'r') as fh:
    for line in fh.readlines():
        line = line.strip()
        if line == '':
            continue

        stack = Stack()
        for n in line.split(' '):
            stack.push(n)

        collect = False
        output = []
        while stack.size() > 0:
            n = stack.pop()

            collect = not collect
            if collect:
                output.append(n)


        print(' '.join(output))

