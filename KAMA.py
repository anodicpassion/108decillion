import time, datetime
from fyers_apiv3 import fyersModel
client_id = "ZHQ4IJL7TI-100"
with open("access_token", "r") as f:
    access_token = f.read()

fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path="")
import matplotlib.pyplot as plt
import numpy as np
from indicators.syncind import SyncInd
from indicators.classic import SMA, Alligator, SmoothMA, RSI, MACD, ATR, WMA, EMA, RMA, VolumeROC, KAMA
from indicators.candle import OHLC
date_today = datetime.datetime.now().strftime("%Y-%m-%d")
date_100_p = (datetime.datetime.now() - datetime.timedelta(days=100)).strftime("%Y-%m-%d")
response = fyers.history(data={
                                "symbol": "NSE:ZEEL-EQ",
                                "resolution": "1",
                                "date_format": "1",
                                "range_from": date_100_p,
                                "range_to": date_today,
                                "cont_flag": "1"
                                })

len(response['candles']), response


candles = np.array(response['candles'])
type(candles), candles

sync = SyncInd( 
    SMA(5),
    # Alligator(show_jaw=False, show_teeth=False)
    KAMA()
)
                
for c in candles:
    sync.append(c)
sync.last_candle().shape
last_candle_show = 0
plt.plot(sync.data()[-last_candle_show:, 4], label="Close", color="blue")
plt.plot(sync.data()[-last_candle_show:, -1], label="Lips", color="red")
plt.plot(sync.Hdata()[-last_candle_show:, -2], label="SMA 5", color="green")
plt.grid()
plt.legend()
plt.show()
