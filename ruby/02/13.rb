# -*- coding: utf-8 -*-

=begin
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
=end

File.open("col1.txt") do |f1|
  File.open("col2.txt") do |f2|
    f1.zip(f2).each do |col1, col2|
      puts "#{col1.chomp}\t#{col2}"
    end
  end
end
