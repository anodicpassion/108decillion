import unittest
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


# class WholeData(unittest.TestCase):
#     def test_something(self):
#         # self.assertEqual(True, False)  # add assertion here
#         for c in candles[:-1]:
#             sync.append(c)
#         print(sync.last_candle())


class LatestData(unittest.TestCase):
    def test_something(self):
        # self.assertEqual(True, False)  # add assertion here

        sync.append(candles[-1])
        print(sync.last_candle())


if __name__ == '__main__':
    unittest.main()
