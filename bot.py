import requests
import time
import os

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

URL = "https://immi.homeaffairs.gov.au/what-we-do/whm-program/status-of-country-caps"

def send_message(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg}
    requests.post(url, data=data)

print("Bot iniciado...")

r = requests.get(URL)
text = r.text.lower()

if "brazil" in text and "open" in text:
    send_message("🚨 VISTO 462 ABRIU PARA O BRASIL!")
else:
    print("Ainda fechado...")
