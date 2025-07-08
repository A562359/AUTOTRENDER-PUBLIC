
from smartapi import SmartConnect
import pyotp
import pandas as pd
from datetime import datetime
import time

API_KEY = "SkyKgmn2"
CLIENT_CODE = "A57362432"
PASSWORD = "Anis@1978"
TOTP_SECRET = "O7VIUTCBCIFCGSRMXCQQK67LPQ"

def login():
    obj = SmartConnect(api_key=API_KEY)
    token = pyotp.TOTP(TOTP_SECRET).now()
    session = obj.generateSession(CLIENT_CODE, PASSWORD, token)
    return obj

def fetch_oi(symbol_token):
    # Dummy structure: You will replace this with actual API logic
    import random
    call_oi = random.randint(1000000, 3000000)
    put_oi = random.randint(1000000, 3000000)
    return call_oi, put_oi

def update_csv(file_path, symbol):
    df = pd.read_csv(file_path) if os.path.exists(file_path) else pd.DataFrame(columns=["Time", "Call OI", "Put OI", "Diff", "PCR", "Signal"])
    now = datetime.now().strftime("%H:%M")
    call_oi, put_oi = fetch_oi(symbol)
    pcr = round(put_oi / call_oi, 2)
    signal = "BUY" if pcr > 1 else "SELL"
    new_row = {"Time": now, "Call OI": call_oi, "Put OI": put_oi, "Diff": put_oi - call_oi, "PCR": pcr, "Signal": signal}
    if df.empty or df["Time"].iloc[-1] != now:
        df = pd.concat([df, pd.DataFrame([new_row])])
        df.to_csv(file_path, index=False)

if __name__ == "__main__":
    update_csv("nifty_pcr.csv", "NIFTY")
    update_csv("banknifty_pcr.csv", "BANKNIFTY")
