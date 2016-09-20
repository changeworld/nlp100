# -*- coding: utf-8 -*-

=begin
08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

* 英小文字ならば(219 - 文字コード)の文字に置換
* その他の文字はそのまま出力

この関数を用い，英語のメッセージを暗号化・復号化せよ．
=end

CIPHER_TABLE = (?a .. ?z).map{|c| (219 - c.ord).chr }.join.freeze

def cipher(str)
  str.tr('a-z', CIPHER_TABLE)
end

sentence = "See you tomorrow, Saki."
puts cipher(sentence)
puts cipher(cipher(sentence))
