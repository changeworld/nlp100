# -*- coding: utf-8 -*-

=begin
06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
=end

module Enumerable
  def ngram(n)
    each_cons(n).to_a
  end
end

words = %w[paraparaparadise paragraph]
x = words[0].gsub(' ', '').chars.ngram(2)
y = words[1].gsub(' ', '').chars.ngram(2)
  
puts "union: #{x | y}"
puts "intersection: #{x & y}"
puts "difference: #{x - y}"
puts "X includes 'se'?: #{x.include?(%w[s e])}"
puts "Y includes 'se'?: #{y.include?(%w[s e])}"
