# -*- coding: utf-8 -*-

=begin
27. 内部リンクの除去
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．
=end

require_relative '26.rb'

def extract27
  Hash.new.tap do |hash|
    extract26.each do |name, value|
      hash[name] = value.gsub(/\[\[ ([^\|\]:]+) (?:\|([^\]]+))? \]\]/x) do
        $2 || $1
      end
    end
  end
end

p extract27
