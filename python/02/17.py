# -*- coding: utf-8 -*-
# 17. １列目の文字列の異なり
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

import sys

prefectures = set()
with open(sys.argv[1]) as f:
    lines = f.readline()
    while lines:
        prefectures.add(lines.split()[0])
        lines = f.readline()
    for prefecture in prefectures:
        print(prefecture)
