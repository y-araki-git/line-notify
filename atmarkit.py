#coding:UTF-8
# モジュールインポート
import requests

def main():
    # Line Notify設定
    url = "https://notify-api.line.me/api/notify"
    token = "アクセストークン"
    headers = {"Authorization" : "Bearer "+ token}
    
    # サイトURLを変数に格納。
    message = "https://www.atmarkit.co.jp/"
    
    # ペイロード送信
    payload = {"message" :  message}
    r = requests.post(url ,headers = headers ,params=payload)

if __name__ == '__main__':
    main()
