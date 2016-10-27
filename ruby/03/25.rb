# -*- coding: utf-8 -*-

=begin
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
=end

def extract25
  template_pattern = /{{基礎情報\s+国\s+(?<params>(?<markup>{{\g<markup>}} | [^{}]*)*)}}/x
  m = template_pattern.match(File.read('uk.txt'))

  Hash.new.tap do |hash|
    m[:params].split(/^\|/).each do |entry|
      next if entry.empty?
      name, value = entry.split(/\s*=\s*/, 2)
      hash[name] = value.chomp
    end
  end
end

p extract25
