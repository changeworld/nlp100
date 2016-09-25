# -*- coding: utf-8 -*-
# 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
import random

def typoglycemia(str):
    typoglycemia_list = []
    for word in str.split():
        if len(word) < 4:
            pass
        else:
            char_list = list(word)
            mid_str = char_list[1:-1]
            random.shuffle(mid_str)
            word = word[0] + "".join(mid_str) + word[-1]
        typoglycemia_list.append(word)
    return " ".join(typoglycemia_list)

print typoglycemia("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .")
