try:
    import numpy as np
except ImportError or ModuleNotFoundError:
    raise ModuleNotFoundError("numpy module not found")
try:
    import datetime
except ImportError or ModuleNotFoundError:
    raise ModuleNotFoundError("datetime module not found")
try:
    from .candle import *
except ImportError or ModuleNotFoundError:
    raise ModuleNotFoundError("indicators.candle module not found")
try:
    from .classic import *
except ImportError or ModuleNotFoundError:
    raise ModuleNotFoundError("indicators.classic module not found")


class SyncInd:
    def __init__(self, *indicators: SMA | SmoothMA | Alligator | RSI | KAMA) -> None:
        if not isinstance(indicators, list) and not isinstance(indicators, tuple):
            raise TypeError("indicators should be of type -> list or tuple")
        # for ind in indicators:
        #     if type(ind) not in available_indicators:
        #         raise TypeError(f"indicator type should be -> {available_indicators}")

        self.__indicators = indicators

        self.__data = np.array([], dtype=np.float32)
        # self.indicator = _Ind(self.__data, sma_length)
        # self.__sma5 = SMA(5)
        # self.__sma15 = SMA(15)

    def append(self, last_candle: np.ndarray) -> None:
        if isinstance(last_candle, np.ndarray):
            candle = OHLC(last_candle)

            if self.__data.shape == (0,):
                temp_array = candle()

                for indic in self.__indicators:
                    temp_array = np.append(temp_array, indic.__call__(candle))

                self.__data = np.array([temp_array], dtype=np.float32)
            else:
                temp_array = candle()
               
                for indic in self.__indicators:
                    temp_array = np.append(temp_array, indic.__call__(candle))

                self.__data = np.append(self.__data, np.array([temp_array]), axis=0)
        else:
            raise TypeError("last_candle should be of type -> numpy.ndarray")

    def last_candle(self) -> np.ndarray:
        return self.__data[-1]

    def data(self) -> np.ndarray:
        return self.__data

    def sync(self, candle: OHLC | np.ndarray) -> bool:
        if isinstance(candle, OHLC):
            candle = candle()
        elif isinstance(candle, np.ndarray):
            candle = candle
        else:
            raise TypeError("candle should be of type -> OHCL | numpy.ndarray")
        if (datetime.datetime.fromtimestamp(int(self.last_candle()[0]))
                <= datetime.datetime.fromtimestamp(int(candle[0]))):

            if (str(datetime.datetime.fromtimestamp(int(candle[0])).strftime("%H:%M"))
                    == str(datetime.datetime.fromtimestamp(int(self.last_candle()[0])).strftime("%H:%M"))):
                print("old updating")

            elif (str(datetime.datetime.fromtimestamp(int(candle[0])).strftime("%H:%M"))
                  != str(datetime.datetime.fromtimestamp(int(self.last_candle()[0])).strftime("%H:%M"))):
                print("new appending")
                self.append(candle)
            return True
        return False
