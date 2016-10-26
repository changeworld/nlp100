# -*- coding: utf-8 -*-

=begin
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．
=end

File.read('uk.txt').scan(/\[\[File:([^|\]]+)(?:\|[^\]]*)*\]\]/) do |file, _|
  puts file
end
