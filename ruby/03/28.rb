# -*- coding: utf-8 -*-

=begin
28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
=end

require_relative '27.rb'

def extract28
  Hash.new.tap do |hash|
    extract27.each do |name, value|
      value = value.gsub(%r!<ref(?:\s[^/>]+)?>.*?</ref>!m, '')
      value = value.gsub(%r!<ref(?:\s[^/>]+)?/>!, '')
      value = value.gsub(%r!<[[:alpha:]]+\s*/>!, '')
      value = value.gsub(%r!&pound;!, '£')
      hash[name] = value
    end
  end
end

p extract28
