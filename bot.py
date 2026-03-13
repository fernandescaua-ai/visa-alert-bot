import os
import requests

print("Bot iniciado")

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

print("Token carregado")
