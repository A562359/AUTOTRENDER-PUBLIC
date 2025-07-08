import pyotp
import time

# 👉 Tera TOTP Secret yahaan daala gaya hai
TOTP_SECRET = "O7VIUTCBCIFCGSRMXCQQK67LPQ"

def get_totp_token():
    totp = pyotp.TOTP(TOTP_SECRET)
    return totp.now()
