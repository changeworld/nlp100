# -*- coding: utf-8 -*-

=begin
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
=end

File.read("uk.txt").scan(/\[\[Category:([^|\]]+)(?:\|[^\]]*)?\]\]/) do |name, _|
  puts name
end
