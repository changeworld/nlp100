# -*- coding: utf-8 -*-

=begin
11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
=end

$<.each_line do |line|
  puts line.gsub("\t", ' ')
end
