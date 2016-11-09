# -*- coding: utf-8 -*-
# 27. 内部リンクの除去
# 26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．

import re

def remove_markup(str):
    str = re.sub(r"'{2,5}", r"", str)
    str = re.sub(r"\[{2}([^|\]]+?\|)*(.+?)\]{2}", r"\2", str)
    return str

with open("uk.txt") as f:
    dict = {}
    lines = f.readline()
    while lines:
        line = re.search("^(.*?)\s=\s(.*)", lines)
        if line is not None:
            dict[line.group(1)] = remove_markup(line.group(2))
        lines = f.readline()
    for k, v in dict.items():
        print("{0}, {1}".format(k, v))
