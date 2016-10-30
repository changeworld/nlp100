# -*- coding: utf-8 -*-

=begin
29. 国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
=end

require 'json'
require 'open-uri'
require_relative '28.rb'

name = extract28['国旗画像']
url = 'https://ja.wikipedia.org/w/api.php?format=json&action=query&continue=&titles=Image:%s&prop=imageinfo&iiprop=url' % URI.escape(name)
res = JSON.parse(open(url) {|data| data.read})
puts res['query']['pages']['-1']['imageinfo'].first['url']
