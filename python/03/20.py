# -*- coding: utf-8 -*-
# 20. JSONデータの読み込み
# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．

import json
import gzip

with gzip.open('jawiki-country.json.gz', 'rb') as f:
    article = f.readline()
    while article:
        json_file = json.loads(article)
        if json_file["title"] == u"イギリス":
            print(json_file["text"])
        article = f.readline()
