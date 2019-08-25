#coding:UTF-8
# モジュールインポート
import requests
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import re

def main():
    # Line Notify設定
    url = "https://notify-api.line.me/api/notify"
    token = "アクセストークン"
    headers = {"Authorization" : "Bearer "+ token}

    # サイトURLを変数に格納
    URL = 'https://japan.zdnet.com/'

    # get()メソッドでデータを取得
    res = requests.get(URL)

    # ステータス確認
    res.status_code == requests.codes.ok

    # reモジュールのfindall()関数を使い正規表現にマッチした箇所を抽出
    subtitles = re.findall(r'<a href="/article/.*/" data-ga_category="zd_top_list_topic"><h3>(.+)</h3></a>', res.text)

    # ファイルオープン
    f = open('zdnet.txt', 'w')

    # URLを出力
    f.write(str(URL) + "\n")

    # 配列に格納された値をファイル書き込み
    for item in subtitles:
        f.write("・" + item + "\n")

    # ファイルクローズ
    f.close()

    # ファイル全体を変数に格納
    with open('zdnet.txt') as f:
        message = f.read()

    # ペイロード送信
    payload = {"message" :  message}
    r = requests.post(url ,headers = headers ,params=payload)

if __name__ == '__main__':
    main()
