# -*- coding: utf-8 -*-

=begin
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
=end

n = ARGV.shift.to_i
$<.lazy.take(n).each{|line| puts line}
