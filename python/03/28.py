# -*- coding: utf-8 -*-
# 28. MediaWikiマークアップの除去
# 27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．

import re

def remove_markup(str):
    str = re.sub(r"'{2,5}", r"", str)
    str = re.sub(r"\[{2}([^|\]]+?\|)*(.+?)\]{2}", r"\2", str)
    str = re.sub(r"\{{2}.+?\|.+?\|(.+?)\}{2}", r"\1 ", str)
    str = re.sub(r"<.*?>", r"", str)
    str = re.sub(r"\[.*?\]", r"", str)
    str = re.sub(r"\&pound;", r"£", str)
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
