# -*- coding: utf-8 -*-

=begin
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
=end

n = ARGV.shift.to_i
arr = $<.to_a
n.times do |i|
  puts arr[arr.length - n + i]
end
