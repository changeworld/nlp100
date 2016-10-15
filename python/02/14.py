# -*- coding: utf-8 -*-
# 14. 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

import sys

with open(sys.argv[2]) as f:
    lines = f.readlines()

for line in lines[:int(sys.argv[1])]:
    print line,
