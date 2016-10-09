# -*- coding: utf-8 -*-

=begin
17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
=end

puts $<.map {|line| line.split("\t")[0]}.sort.uniq
