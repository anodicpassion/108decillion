import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, Reshape, Input, Flatten
from sklearn.model_selection import train_test_split
import threading
import concurrent.futures
import time, datetime
from fyers_apiv3 import fyersModel

client_id = "ZHQ4IJL7TI-100"
with open("access_token", "r") as f:
    access_token = f.read()

fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path="")

import matplotlib.pyplot as plt
import numpy as np
import os

from indicators.syncind import SyncInd
from indicators.classic import SMA, Alligator, SmoothMA, RSI, MACD, ATR, WMA, EMA, RMA, VolumeROC, KAMA
from indicators.candle import OHLC

last_candles_count = 8
next_candles_count = 5

date_today = datetime.datetime.now().strftime("%Y-%m-%d")
date_yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
date_100_p = (datetime.datetime.now() - datetime.timedelta(days=100)).strftime("%Y-%m-%d")

response = fyers.history(data={
    "symbol": "NSE:ZEEL-EQ",
    "resolution": "1",
    "date_format": "1",
    "range_from": date_100_p,
    "range_to": date_yesterday,
    "cont_flag": "1"
})

date_temp = []
final_candles_list = []
for i in response['candles']:
    if i[0] not in date_temp:
        final_candles_list.append(i)
        date_temp.append(i[0])
del date_temp
len(final_candles_list)

candles = np.array(final_candles_list)

sync = SyncInd(SMA(5), KAMA(highlight=True))
for c in candles:
    sync.append(c)

model = tf.keras.models.load_model("26NOV_2.keras")
model.summary()

new_ind = sync.data().shape[0]


def fetch():
    response_rt = fyers.history(data={
        "symbol": "NSE:ZEEL-EQ",
        "resolution": "1",
        "date_format": "1",
        "range_from": date_today,
        "range_to": date_today,
        "cont_flag": "1"
    })



def predict():
    X_test_seq = []
    if len(sync.data()[new_ind:]) >= last_candles_count+1:
        first_candle = sync.data()[-(last_candles_count+1):]
        for i in range(last_candles_count, 0, -1):
            X_test_seq.append(first_candle - sync.data()[-i])
        print("x shape: ", np.array(X_test_seq).shape)
        print(model.predict(np.array(X_test_seq)))
    print("cannot predict")


print("current time:", datetime.datetime.now().strftime("%H:%M:%S"))
# while 1:
#     time.sleep(1)
#     if 60 - int(datetime.datetime.now().strftime("%S")) > 55:
#         break
#     else:
#         print('Starting in:', 60 - int(datetime.datetime.now().strftime("%S")), "s")

while 1:
    fetch()
    predict()
    # time.sleep(1)
    # break