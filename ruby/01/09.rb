# -*- coding: utf-8 -*-

=begin
09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
=end

def typoglycemia(str)
  str.split().map {|word|
    if word.size <= 4
      word
    else
      [word[0], word[1..-2].chars.shuffle, word[-1]].flatten.join
    end
  }.join(' ')
end
  
puts typoglycemia("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .")
