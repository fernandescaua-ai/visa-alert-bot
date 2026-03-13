import requests
import time
import os

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

URL = "https://immi.homeaffairs.gov.au/what-we-do/whm-program/status-of-country-caps"

def send_message(text):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": text}
    )

while True:
    r = requests.get(URL)
    text = r.text.lower()

    if "brazil" in text and "open" in text:
        send_message("🚨 ATENÇÃO: Visto 462 abriu para o Brasil!")
        break

    print("Ainda fechado...")
    time.sleep(20)
