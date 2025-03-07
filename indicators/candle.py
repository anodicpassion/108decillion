import numpy as np


class OHLC:
    def __init__(self, candle: np.ndarray) -> None:
        if candle is None or isinstance(candle, np.ndarray) is False:
            raise ValueError("candle should be non-empty array of type -> numpy.ndarray")

        if not candle.shape == (6, ):
            raise ValueError("candle should have shape (6, ) of type numpy.ndarray.")

        if isinstance(candle[0], float) and candle[0] > 0:
            self.__datetime = candle[0]
        else:
            raise TypeError("date should be in POSIX time")

        if isinstance(candle[1], int) or isinstance(candle[1], float):
            self.__open = round(float(candle[1]), 2)
        else:
            raise TypeError("candle open should be of type int or float")

        if isinstance(candle[2], int) or isinstance(candle[2], float):
            self.__high = round(float(candle[2]), 2)
        else:
            raise TypeError("candle open should be of type int or float")

        if isinstance(candle[3], int) or isinstance(candle[3], float):
            self.__low = round(float(candle[3]), 2)
        else:
            raise TypeError("candle open should be of type int or float")

        if isinstance(candle[4], int) or isinstance(candle[4], float):
            self.__close = round(float(candle[4]), 2)
        else:
            raise TypeError("candle open should be of type int or float")

        if isinstance(candle[5], int) or isinstance(candle[5], float):
            self.__volume = round(float(candle[5]), 2)
        else:
            raise TypeError("candle open should be of type int or float")

    def date(self) -> int:
        return int(self.__datetime)

    def open(self) -> float:
        return round(float(self.__open), 2)

    def high(self) -> float:
        return round(float(self.__high), 2)

    def low(self) -> float:
        return round(float(self.__low), 2)

    def close(self) -> float:
        return round(float(self.__close), 2)

    def volume(self) -> float:
        return round(float(self.__volume), 2)

    def __call__(self, *args, **kwargs) -> np.ndarray:
        return np.array([self.__datetime, round(self.__open, 2), round(self.__high, 2), round(self.__low, 2), round(self.__close, 2), round(self.__volume, 2)],
                        dtype=np.float32)
