import os
import time
import requests
from fyers_apiv3 import fyersModel

client_id = "ZHQ4IJL7TI-100"
secret_key = "Q97YMM41F5"
redirect_uri = "https://anodicpassion.pythonanywhere.com/naW4uZnllcnMuaW4iLCJpYXQiOjE3Mzk5MDgyMzksImV4c/"
response_type = "code"
state = "sample_state"
grant_type = "authorization_code"


def authenticate() -> str:
    access_token = get_token()
    fyr = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path="")
    market_status = fyr.market_status()
    if market_status["code"] != 200:
        access_token = generate_token()
        return access_token["access_token"]
    return access_token


def generate_token() -> dict:
    session = fyersModel.SessionModel(
        client_id=client_id,
        secret_key=secret_key,
        redirect_uri=redirect_uri,
        response_type=response_type
    )

    response = session.generate_authcode()
    os.system(f'''open "{str(response)}"''')
    # print("Click this link:\n", response)

    response = requests.post(redirect_uri, json={})
    while len(response.json()["auth_code"]) == 0:
        response = requests.post(redirect_uri, json={})
        time.sleep(1)

    session = fyersModel.SessionModel(
        client_id=client_id,
        secret_key=secret_key,
        redirect_uri=redirect_uri,
        response_type=response_type,
        grant_type=grant_type
    )

    auth_code = response.json()["auth_code"]
    session.set_token(auth_code)
    response = session.generate_token()

    with open("access_token", "w") as f:
        f.write(response['access_token'])
    return response


def get_token() -> str:
    with open("access_token", "r") as f:
        access_token = f.read()
    return access_token


if __name__ == "__main__":
    rep = authenticate()
