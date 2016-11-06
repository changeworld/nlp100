# -*- coding: utf-8 -*-
# 26. 強調マークアップの除去
# 25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．

import re

with open("uk.txt") as f:
    dict = {}
    lines = f.readline()
    while lines:
        line = re.search("^(.*?)\s=\s(.*)", lines)
        if line is not None:
            dict[line.group(1)] = re.sub(r"'{2,5}", r"", line.group(2))
        lines = f.readline()
    for k, v in dict.items():
        print "{0}, {1}".format(k, v)
