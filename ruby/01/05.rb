# -*- coding: utf-8 -*-

=begin
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
=end

module Enumerable
  def ngram(n)
    each_cons(n).to_a
  end
end

words = 'I am an NLPer'
p words.split.ngram(2)
p words.gsub(' ', '').chars.ngram(2)
