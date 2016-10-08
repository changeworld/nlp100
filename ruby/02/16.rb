# -*- coding: utf-8 -*-

=begin
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
=end

n = ARGV.shift.to_i
arr = $<.to_a
suffix = 'aa'

while arr != []
  File.open("x#{suffix}", 'w') do |out|
    n.times do
      break if arr == []
      out.print "#{arr.shift}"
    end
  end
  suffix.succ!
end
