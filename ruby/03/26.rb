# -*- coding: utf-8 -*-

=begin
26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．
=end

require_relative '25.rb'

def extract26
  Hash.new.tap do |hash|
    extract25.each do |name, value|
      hash[name] = value.gsub(/('{2,3}|'{5})([^']+)\1/, '\2')
    end
  end
end

p extract26
