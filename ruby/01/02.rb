# -*- coding: utf-8 -*-

=begin
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
=end

strs = %w[パトカー タクシー]
puts strs.map(&:chars).transpose.map{|i| i.join}.join
