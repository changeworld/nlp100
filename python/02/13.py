# -*- coding: utf-8 -*-
# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

with open("col1.txt") as f1, open("col2.txt") as f2:
    lines1, lines2 = f1.readlines(), f2.readlines()

with open("col1-col2.txt", "w") as writer:
    for col1, col2 in zip(lines1, lines2):
        writer.write("\t".join([col1.rstrip(), col2]))
