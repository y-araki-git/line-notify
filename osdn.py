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

    # OSDN magazineのURLを変数に格納
    URL = 'https://mag.osdn.jp/news/'

    # requests.get()でHTMLを取得
    result = requests.get(URL)

    # BeautifulSoupの機能、html.parserでHTMLやXMLをパースできる。
    data1 = BeautifulSoup(result.text, 'html.parser')

    # find_allでclassを指定し、見出しを取得
    data2 = data1.find_all("h2", class_="entry-title")

    # ファイルオープン
    f = open('osdn.txt', 'w')

    # URLを出力
    f.write(str(URL) + "\n")

    # 配列に格納された値をファイル書き込み
    for item in data2:
        f.write("・" + item.getText() + "\n")

    # ファイルクローズ
    f.close()

    # ファイル全体を変数に格納
    with open('osdn.txt') as f:
        message = f.read()

    # ペイロード送信
    payload = {"message" :  message}
    r = requests.post(url ,headers = headers ,params=payload)

if __name__ == '__main__':
    main()
