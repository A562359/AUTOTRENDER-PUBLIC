from SmartApi import SmartConnect
from autototp import get_totp_token  # Import TOTP token generator

# ✅ API details
API_KEY = "Pe84PVPR"
CLIENT_CODE = "A57362432"
PASSWORD = "Anis@1978"
SECRET_KEY = "ab7cd6200-c641-4f19-a72e-305f531214d4"

# ✅ SmartConnect Object
obj = SmartConnect(api_key=API_KEY)

# ✅ Generate session using auto TOTP
session = obj.generateSession(CLIENT_CODE, PASSWORD, get_totp_token())
refreshToken = session['data']['refreshToken']

# ✅ Get feed token
feedToken = obj.getfeedToken()

# ✅ Function to fetch option chain data
def get_option_chain():
    # Replace with real tokens for expiry
    calls = ["99926008"]  # Example Call Option Token
    puts = ["99926009"]   # Example Put Option Token

    data = []
    for token in calls + puts:
        ltp = obj.ltpData("NFO", token, "NIFTY")
        data.append({
            "Token": token,
            "LTP": ltp['data']['ltp'],
            "OI": ltp['data']['openInterest']
        })
    return data
