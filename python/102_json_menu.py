# pylint: disable=invalid-name, missing-docstring

import json
import sys

with open(sys.argv[1], 'r') as fh:
    for line in fh.readlines():
        line = line.strip()
        if line == '':
            continue

        menu = json.loads(line)

        items = menu['menu']['items']
        print(
            sum(
                item['id']
                for item in items
                if item is not None and 'label' in item
            )
        )

