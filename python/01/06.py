# -*- coding: utf-8 -*-
# 06. 集合
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
sentence1 = 'paraparaparadise'
sentence2 = 'paragraph'

def ngram(input, n):
    l = len(input) - n + 1
    list = []
    for i in range(0, l):
        list.append(input[i:i+n])
    return list

X = set(ngram(sentence1, 2))
Y = set(ngram(sentence2, 2))

print('union: {0}'.format(list(X.union(Y))))
print('intersection: {0}'.format(list(X.intersection(Y))))
print('difference: {0}'.format(list(X.difference(Y))))
print("X includes 'se'?: {0}".format('se' in X))
print("Y includes 'se'?: {0}".format('se' in Y))
