# -*- coding: utf-8 -*-

=begin
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
=end

File.open("col1.txt", "w") do |f1|
  File.open("col2.txt", "w") do |f2|
    $<.each_line do |line|
      cols = line.split("\t")
      f1.puts cols[0]
      f2.puts cols[1]
    end
  end
end
