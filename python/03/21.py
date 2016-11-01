# -*- coding: utf-8 -*-
# 21. カテゴリ名を含む行を抽出
# 記事中でカテゴリ名を宣言している行を抽出せよ．

with open("uk.txt") as f:
    lines = f.readline()
    while lines:
        if "Category" in lines:
            print(lines, end="")
        lines = f.readline()
