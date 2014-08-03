__author__ = 'ASmolyakov'

import urllib.parse
import urllib.request
import urllib.response

YM_API_URL = "https://money.yandex.ru/api"
ACCESS_TOKEN = ""


def account_info():
    # Prepare request data
    payload = {}
    headers = {"Authorization": "Bearer " + ACCESS_TOKEN}
    binary_data = urllib.parse.urlencode(payload).encode("utf-8")

    # Make request
    request = urllib.request.Request(YM_API_URL + '/account-info', binary_data, headers)
    response = urllib.request.urlopen(request)

    # Convert response to string
    response_json = response.read().decode("utf-8")

    return response_json