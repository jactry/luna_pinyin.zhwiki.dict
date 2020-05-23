#!/usr/bin/env python3

import sys
import re
import opencc

converter = opencc.OpenCC('s2t.json')

FILE = sys.argv[1]

HANZI_RE = re.compile('^[\u4e00-\u9fa5]+$')
YAML_HEADER = "---\nname: luna_pinyin.zhwiki.dict.yaml\nversion: \"2020.05.23\"\nsort: by_weight\nuse_preset_vocabulary: true\n...\n"
print(YAML_HEADER)
count = 0
with open(FILE) as f:
    for line in f:
        line = line.rstrip("\n")
        if not HANZI_RE.match(line):
            continue

        print(converter.convert(line))
        count += 1
        if count % 1000 == 0:
            print(str(count) + " converted", file=sys.stderr)

if count % 1000 != 0:
    print(str(count) + " converted", file=sys.stderr)
