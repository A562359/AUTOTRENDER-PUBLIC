from SmartApi import SmartConnect
from autototp import get_totp_token
import pandas as pd

API_KEY = "Pe84PVPR "
CLIENT_CODE = "A57362432"
PASSWORD = "Anis@1978"
SECRET_KEY = "b7cd6200-c641-4f19-a72e-305f531214d4"

obj = SmartConnect(api_key=API_KEY)
session = obj.generateSession(CLIENT_CODE, PASSWORD, get_totp_token())
refreshToken = session['data']['refreshToken']
feedToken = obj.getfeedToken()

def get_pcr_data():
    instruments = [
        {"exchange": "NFO", "symboltoken": "99926009"},  # Nifty Put
        {"exchange": "NFO", "symboltoken": "99926008"}   # Nifty Call
    ]

    total_put_oi = 0
    total_call_oi = 0

    for inst in instruments:
        ltp = obj.ltpData(inst['exchange'], inst['symboltoken'], "NIFTY")
        oi = ltp['data']['openInterest']
        if "Put" in inst['symboltoken']:
            total_put_oi += int(oi)
        else:
            total_call_oi += int(oi)

    pcr = round(total_put_oi / total_call_oi, 2) if total_call_oi != 0 else 0
    return total_put_oi, total_call_oi, pcr
