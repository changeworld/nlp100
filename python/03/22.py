# -*- coding: utf-8 -*-
# 22. カテゴリ名の抽出
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

import re

with open("uk.txt") as f:
    lines = f.readline()
    while lines:
        line = re.search("^\[\[Category:(.*?)(|\|.*)\]\]$", lines)
        if line is not None:
            print(line.group(1))
        lines = f.readline()
