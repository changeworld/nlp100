# -*- coding: utf-8 -*-

=begin
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
=end

File.foreach('uk.txt').grep(/\[\[Category:/) do |line|
  puts line
end
