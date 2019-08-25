#coding:UTF-8
# モジュールインポート
import requests
import urllib.request, urllib.error
from bs4 import BeautifulSoup

def main():
    # Line Notify設定
    url = "https://notify-api.line.me/api/notify"
    token = "アクセストークン"
    headers = {"Authorization" : "Bearer "+ token}
    
    # サイトURLを変数に格納。
    URL = "https://blog.tokumaru.org/"
    
    # サイトURLにアクセス。戻り値はアクセスした結果やHTMLを返す。
    R = urllib.request.urlopen(URL)
    
    # アクセス結果からHTMLを取り出し、BeautifulSoupの機能でhtmlパースする。
    soup = BeautifulSoup(R, "html.parser")
    
    # CSSセレクタを使って指定した場所を表示。.textでhtmlではなくtext形式となる。
    line = soup.select_one("#Blog1 > div.blog-posts.hfeed > div:nth-child(1) > div > div.post-outer > div > h3 > a").text
    
    # ファイルオープン
    f = open('tokumaru.txt', 'w')

    # URLを出力
    f.write(str(URL) + "\n")

    # 配列に格納された値をファイル書き込み
    f.write(line + "\n")

    # ファイルクローズ
    f.close()

    # ファイル全体を変数に格納
    with open('tokumaru.txt') as f:
        message = f.read()
    
    # ペイロード送信
    payload = {"message" :  message}
    r = requests.post(url ,headers = headers ,params=payload)

if __name__ == '__main__':
    main()
