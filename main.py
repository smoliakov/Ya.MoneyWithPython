__author__ = 'ASmolyakov'

import json
import yamoney

# Define const
yamoney.ACCESS_TOKEN = "410011161616877.70CB207784C63018088136F3E7701225E70FD669B4EEB8E24FCAB16BA97EEFACCD91070D5F67D91D5AB82CC8AEC0DB7A394536ECB0BAFCEE8B620D4EC83D9721158CF9BE415E141056BF292F4A39A2BA3025D098311D7511119059939C74AC14CB9CC9E90A07ECE547B208214EAC21FC2477207F3C827C4F68D6B0F939DDC19D"

# Make request
response_json = yamoney.account_info()

# Load JSON
user_data = json.loads(response_json)

# Print user info
print("User #{0:s} has {1:.2f} RUB.".format(user_data.get("account"), user_data.get("balance")))

# Print whole account info
print(json.dumps(user_data, indent=4, sort_keys=True))

