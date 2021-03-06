# -*- coding: utf-8 -*-

=begin
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
=end

freq = Hash.new(0)
$<.map {|line|
  pref, _ = line.split("\t")
  freq[pref] += 1
}
freq.sort{|(k1, v1), (k2, v2)| v2 <=> v1}.each do |pref, count|
  puts "#{count} #{pref}"
end
