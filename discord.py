import requests
from settings import DISCORD_WEBHOOK_URL


def send_to_discord(message: str):
    payload = {"content": message}
    if DISCORD_WEBHOOK_URL:
        res = requests.post(DISCORD_WEBHOOK_URL, json=payload)
    else:
        raise Exception("DISCORDのURLが設定されていません")
    if not res.ok:
        print("DISCORDへの送信に失敗しました")
