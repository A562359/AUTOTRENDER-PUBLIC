import pyotp
import time

TOTP_SECRET = "O7VIUTCBCIFCGSRMXCQQK67LPQ"  # <-- Yahan pe secret likhna hai

def get_totp_token():
    totp = pyotp.TOTP(TOTP_SECRET)
    return totp.now()
