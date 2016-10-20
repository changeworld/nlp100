# -*- coding: utf-8 -*-
# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．

import sys
import collections

freq = collections.defaultdict(int)
with open(sys.argv[1]) as f:
    lines = f.readline()
    while lines:
        freq[lines.split()[0]] += 1
        lines = f.readline()
    for k, v in sorted(freq.items(), key=lambda x: x[1], reverse=True):
        print v, k
