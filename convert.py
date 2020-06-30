#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
import opencc

FILE = sys.argv[1]
VERSION = sys.argv[2]
DICT_FILE = sys.argv[3]

HANZI_RE = re.compile('^[\u4e00-\u9fa5]+$')
YAML_HEADER = "# encoding: utf-8\n\n---\nname: luna_pinyin.zhwiki\nversion: \"%s\"\nsort: by_weight\nuse_preset_vocabulary: true\n...\n\n" % (VERSION)
_LIST_PAGE_ENDINGS = [
    '一览',
    '一覧',
    '一覽',
    '一览表',
    '一覽表',
    '登场人物',
    '登場人物',
    '登埸人物',
    '角色表',
    '列表',
    '歧義表',
    '人物表',
    '人物名单',
    '人物名單',
]

def convert_to_dict(source_file, dict_file):
    converter = opencc.OpenCC('s2t.json')
    count = 0
    dicts = []
    with open(source_file) as f:
        for line in f:
            line = line.rstrip("\n")
            if not HANZI_RE.match(line):
                continue

            # Skip single character & too long pages
            if not 1 < len(line) < 9:
                continue

            # Skip list pages
            if line.endswith(tuple(_LIST_PAGE_ENDINGS)):
                continue

            dicts.append(converter.convert(line))
            count += 1
            if count % 100000 == 0:
                print(str(count) + " converted", file=sys.stderr)

    if count % 1000 != 0:
        print(str(count) + " converted", file=sys.stderr)

    reordered_dicts = list(set(dicts))
    reordered_dicts.sort()
    with open(dict_file, 'w') as f:
        f.write(YAML_HEADER)
        f.writelines("%s\n" % word for word in reordered_dicts)

if __name__ == "__main__":
    convert_to_dict(FILE, DICT_FILE)
