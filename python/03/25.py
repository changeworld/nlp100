# -*- coding: utf-8 -*-
# 25. テンプレートの抽出
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

import re

with open("uk.txt") as f:
    dict = {}
    lines = f.readline()
    while lines:
        line = re.search("^(.*?)\s=\s(.*)", lines)
        if line is not None:
            dict[line.group(1)] = line.group(2)
        lines = f.readline()
    for k, v in dict.items():
        print "{0}, {1}".format(k, v)
