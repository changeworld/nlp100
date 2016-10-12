# -*- coding: utf-8 -*-
# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

import sys

with open(sys.argv[1]) as f:
    str = f.read()

print(str.replace("\t", " "))
