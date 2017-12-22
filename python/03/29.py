# -*- coding: utf-8 -*-
# 29. 国旗画像のURLを取得する
# テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）

import re
import requests

def remove_markup(str):
    str = re.sub(r"'{2,5}", r"", str)
    str = re.sub(r"\[{2}([^|\]]+?\|)*(.+?)\]{2}", r"\2", str)
    str = re.sub(r"\{{2}.+?\|.+?\|(.+?)\}{2}", r"\1 ", str)
    str = re.sub(r"<.*?>", r"", str)
    str = re.sub(r"\[.*?\]", r"", str)
    str = re.sub(r"\&pound;", r"£", str)
    return str

with open("uk.txt") as f:
    dict = {}
    lines = f.readline()
    while lines:
        line = re.search("^(.*?)\s=\s(.*)", lines)
        if line is not None:
            dict[line.group(1)] = remove_markup(line.group(2))
        lines = f.readline()

url = "https://ja.wikipedia.org/w/api.php"
payload = {"format": "json",
           "action": "query",
           "titles": "Image:{0}".format(dict[u"|国旗画像"]),
           "prop": "imageinfo",
           "iiprop": "url"}
json_data = requests.get(url, params=payload).json()
print(json_data["query"]["pages"]["-1"]["imageinfo"][0]["url"])
