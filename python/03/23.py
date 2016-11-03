# -*- coding: utf-8 -*-
# 23. セクション構造
# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．

import re

with open("uk.txt") as f:
    lines = f.readline()
    while lines:
        line = re.search("^(=+)\s*(.*?)\s*(=+)$", lines)
        if line is not None:
            print "name={0}, level={1}".format(line.group(2), len(line.group(1)) - 1)
        lines = f.readline()
