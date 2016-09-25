# -*- coding: utf-8 -*-
# 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
# * 英小文字ならば(219 - 文字コード)の文字に置換
# * その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．
def cipher(str):
    out = ""
    for char in str:
        out += chr(219 - ord(char)) if char.islower() else char
    return out

sentence = 'See you tomorrow, Saki.'
print cipher(sentence)
print cipher(cipher(sentence))
