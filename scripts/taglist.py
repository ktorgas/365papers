#!/usr/bin/env python3

import glob
import yaml

files = glob.glob('./_posts/*.md')

tags = []

for f in files:
    lines = open(f, 'r').readlines()
    info = yaml.load(
        "".join(lines[1:lines.index("---\n", 2)])
    )
    tags.extend(info['tags'])

tags = sorted(list(set(tags)))
print(" ".join(tags))
