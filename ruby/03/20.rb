# -*- coding: utf-8 -*-

=begin
20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
=end
require 'zlib'
require 'json'

f = File.open('jawiki-country.json.gz')
gz = Zlib::GzipReader.new(f)
uk = gz.map(&JSON.method(:parse)).
  find{|article| article['title'] == 'イギリス'}
raise 'no article about "イギリス"' unless uk
puts uk['text']
gz.close
