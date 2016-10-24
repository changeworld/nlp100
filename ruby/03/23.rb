# -*- coding: utf-8 -*-

=begin
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
=end

File.foreach('uk.txt') do |line|
  next unless s = /^(={2,})\s*([^=]+)\s*\1/o.match(line)
  puts "name=#{s[2]}, level=#{s[1].size - 1}"
end
