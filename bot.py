import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = "@tgminiappsupdates"

MESSAGE = """🔥 Buying Old Tinder Accounts 🔥

📅 2010 – 2024 (All Months) = 22 USDT
📅 2025 (First 5 Months) = 17 USDT

✅ All account ages accepted

📌 We need old Tinder accounts.
📌 2025 (Months 7–12) Female Accounts:
👉 @Kreegyr

🚨 ALSO BUYING ASHLEY MADISON FEMALE ACCOUNTS.
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": MESSAGE
    }
)

print(response.text)
