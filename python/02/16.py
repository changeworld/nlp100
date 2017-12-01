# -*- coding: utf-8 -*-
# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

import sys, math

N = int(sys.argv[1])

with open(sys.argv[2]) as f:
    lines = f.readlines()

n = int(math.ceil(len(lines) / N))
i = 0
for i in range(N):
    file = "x%s" % (i + 1)
    out = open(file, "w")
    for j in range(n):
        try:
            out.write(lines[i + j])
        except:
            break
    i += n
    out.close()
