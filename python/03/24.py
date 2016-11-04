# -*- coding: utf-8 -*-
# 24. ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ．

import re

with open("uk.txt") as f:
    lines = f.readline()
    while lines:
        line = re.search("File:(.*?)\|", lines)
        if line is not None:
            print "{0}".format(line.group(1))
        lines = f.readline()
