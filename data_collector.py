from fyers_apiv3 import fyersModel
import datetime
import time

client_id = "ZHQ4IJL7TI-100"
with open("access_token", "r") as f:
    access_token = f.read()

fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path="")

data = {
    "symbol": "NSE:ZEEL-EQ",
    "resolution": "1",
    "date_format": "1",
    "range_from": datetime.datetime.now().strftime('%Y-%m-%d'),
    "range_to": datetime.datetime.now().strftime('%Y-%m-%d'),
    "cont_flag": "1"
}


def loop():
    with open("data_archive", "a") as arc:
        while 1:
            response = fyers.history(data=data)
            print(response)
            arc.write(datetime.datetime.now().strftime('date_%Y_%m_%d_time_%H_%M_%S = ') + str(response) + "\n")
            time.sleep(15)


def main(start_hour: int = 9, start_minute: int = 15):
    target_hour = start_hour
    target_minute = start_minute
    while 1:
        now = datetime.datetime.now()
        if now.hour == target_hour and now.minute >= target_minute:
            loop()
            break
        print("waiting")
        time.sleep(0)


if __name__ == '__main__':
    main()
