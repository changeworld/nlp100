# -*- coding: utf-8 -*-
# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
sentence = 'I am an NLPer'

def ngram(input, n):
    l = len(input)
    for i in xrange(l - 1):
        print (input[i:i+n], end=' ')
    print ('')

ngram(sentence.split(), 2)
ngram(sentence.replace(' ', ''), 2)
