import copy

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

        self.__data = np.array([], dtype=np.float64)
        self.__data_temp = np.array([], dtype=np.float64)
        self.__previous_cnd = None
        # self.indicator = _Ind(self.__data, sma_length)
        # self.__sma5 = SMA(5)
        # self.__sma15 = SMA(15)

    def indicators(self):
        return self.__indicators

    def append(self, last_candle: np.ndarray) -> None:
        if isinstance(last_candle, np.ndarray):
            candle = OHLC(last_candle)
            if self.__data.shape == (0,):
                temp_array = candle()

                for indic in self.__indicators:
                    temp_array = np.append(temp_array, indic.__call__(candle))

                self.__data = np.array([temp_array], dtype=np.float64)
            else:
                temp_array = candle()

                for indic in self.__indicators:
                    temp_array = np.append(temp_array, indic.__call__(candle))

                self.__data = np.append(self.__data, np.array([temp_array]), axis=0)
        else:
            raise TypeError("last_candle should be of type -> numpy.ndarray")

    def _update(self, last_candle: np.ndarray, update_index: int = -1) -> None:
        if isinstance(last_candle, np.ndarray):
            candle = OHLC(last_candle)
            temp_indicator = copy.deepcopy(self.__indicators)
            self.__data_temp = self.__data.copy()
            if self.__data_temp[-1][0] < candle()[0]:
                self.__data_temp = np.append(self.__data_temp, [np.zeros_like(self.__data_temp[-1])], axis=0)
            if self.__data_temp.shape == (0,):
                temp_array = candle()

                for indic in temp_indicator:
                    temp_array = np.append(temp_array, indic.__call__(candle))

                self.__data_temp = np.array([temp_array], dtype=np.float64)
            else:
                temp_array = candle()

                for indic in temp_indicator:
                    temp_array = np.append(temp_array, indic.__call__(candle))

                self.__data_temp[update_index] = np.array([temp_array])
        else:
            raise TypeError("last_candle should be of type -> numpy.ndarray")

    def last_candle(self) -> np.ndarray:
        return self.__data[-1]

    def data(self) -> np.ndarray:
        return self.__data

    # def sync(self, candle: OHLC | np.ndarray) -> bool:
    #     if isinstance(candle, OHLC):
    #         candle = candle()
    #     elif isinstance(candle, np.ndarray):
    #         candle = candle
    #     else:
    #         raise TypeError("candle should be of type -> OHCL | numpy.ndarray")
    #     if int(self.last_candle()[0]) <= int(candle[0]):
    #         if int(self.last_candle()[0]) == int(candle[0]):
    #             print("old updating")
    #             self._update(candle, -1)
    #         elif int(self.last_candle()[0]) != int(candle[0]):
    #             print("new ")
    #             self.append(candle)
    #         return True
    #     return False

    def sync(self, last_candles: np.array):
        last = last_candles[-1]
        last2 = last_candles[-2]
        if isinstance(last, OHLC):
            last = last()
        elif isinstance(last, np.ndarray):
            last = last
        else:
            raise TypeError("candle should be of type -> OHCL | numpy.ndarray")
        if isinstance(last2, OHLC):
            last2 = last2()
        elif isinstance(last2, np.ndarray):
            last2 = last2
        else:
            raise TypeError("candle should be of type -> OHCL | numpy.ndarray")

        if not all(self.last_candle()[:6] == last2):
            if last2[0] > self.last_candle()[0]:
                self.append(last2)

        if self.last_candle()[0] < last[0]:
            self._update(last)

    def sync_data(self):
        if not self.__data_temp.shape[0]:
            self.__data_temp = self.__data.copy()
        return self.__data_temp
