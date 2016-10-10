# -*- coding: utf-8 -*-

=begin
18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
=end

$<.map {|line| line.split("\t")}.sort_by {|_, _, num, _|
  -num.to_f
}.each do |data|
  puts data.join("\t")
end
