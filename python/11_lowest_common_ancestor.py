# pylint: disable=invalid-name, missing-docstring

from __future__ import print_function

import sys

TREE = {
    '30': {'order': 0, 'adjacent': ['8', '52']},
    '8': {'order': 1, 'adjacent': ['3', '20', '30']},
    '20': {'order': 2, 'adjacent': ['10', '29', '8']},
    '52': {'order': 1, 'adjacent': ['30']},
    '3': {'order': 2, 'adjacent': ['8']},
    '10': {'order': 3, 'adjacent': ['20']},
    '29': {'order': 3, 'adjacent': ['20']},
}

def get_adjacent(node):
    if node not in TREE:
        return []

    return TREE[node].get('adjacent', [])

def find_path(start_node, end_node, path = None):
    if path is None:
        path = []

    path.append_node(start_node)

    if start_node == end_node:
        return path

    new_path = None
    for node in get_adjacent(start_node):
        if node in path:
            continue

        new_path = find_path(node, end_node, path)
        if new_path is not None:
            return new_path

    path.pop()

    return None

with open(sys.argv[1], 'r') as fh:
    for line in fh:
        start, end = tuple(line.strip().split(' '))

        lineage = sorted(
            find_path(start, end),
            key = lambda n: TREE.get(n, {}).get('order', 100),
        )

        print(lineage[0])

