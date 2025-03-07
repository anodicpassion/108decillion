from indicators.syncind import SyncInd
from indicators.classic import SMA, Alligator, SmoothMA
import numpy as np
from fyers_apiv3 import fyersModel
import time, datetime

client_id = "ZHQ4IJL7TI-100"
with open("access_token", "r") as f:
    access_token = f.read()

fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path="")

date_today = datetime.datetime.now().strftime("%Y-%m-%d")
date_100_p = (datetime.datetime.now() - datetime.timedelta(days=100)).strftime("%Y-%m-%d")

response = fyers.history(data={"symbol": "NSE:ZEEL-EQ",
                               "resolution": "1",
                               "date_format": "1",
                               "range_from": date_100_p,
                               "range_to": date_today,
                               "cont_flag": "1"
                               })


candles = np.array(response['candles'])

sync = SyncInd(SMA(5),
               SMA(15),
               Alligator(jaw_offset=1, lips_offset=1, teeth_offset=1),
               SmoothMA(7))
for c in candles:
    sync.append(c)

while 1:
    time.sleep(1)
    sync.append(np.array(fyers.history(data={"symbol": "NSE:ZEEL-EQ",
                                             "resolution": "1",
                                             "date_format": "1",
                                             "range_from": date_100_p,
                                             "range_to": date_today,
                                             "cont_flag": "1"
                                             })['candles'][-1]))
    l = sync.last_candle()
    print(f"{l[0]} {l[1]} {l[3]} {l[4]} {l[5]} {l[6]} {l[7]} {l[8]} {l[9]} {l[10]} {l[11]}", end="\n\n")
