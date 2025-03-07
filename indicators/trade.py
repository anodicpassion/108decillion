from .candle import *
from .classic import *


class Balance:
    def __init__(self, balance: float | int) -> None:
        if not isinstance(balance, float) and not isinstance(balance, int):
            raise TypeError("__balance should be of type -> int | float")
        self.__balance = balance

    def __call__(self) -> float | int:
        return self.__balance

    def __add__(self, amount: float | int) -> bool:
        if not isinstance(amount, float) and not isinstance(amount, int):
            raise TypeError("amount should be of type -> int | float")
        self.__balance = self.__balance + amount
        return True

    def __sub__(self, amount: float | int) -> bool:
        if not isinstance(amount, float) and not isinstance(amount, int):
            raise TypeError("amount should be of type -> int | float")
        if self.__balance >= amount:
            self.__balance = self.__balance - amount
            return True
        else:
            return False


class Broker:
    def __init__(self, balance: Balance) -> None:

        if not isinstance(balance, Balance):
            raise TypeError("__balance should be of type -> Balance")

        self.__balance = balance
        self.__profit = 0
        self.__trade_book = {}

    def __call__(self) -> int:
        j = 0
        while j in self.__trade_book.keys():
            j += 1
        self.__trade_book[j] = []
        return j

    def buy(self, trade_id: int, candle: OHLC | float | int) -> None:
        if not isinstance(trade_id, int):
            raise TypeError("trade_id should be of type -> int")
        if isinstance(candle, OHLC):
            buy_price = SMA(1)
        elif isinstance(candle, float) or isinstance(candle, int):
            buy_price = candle
        else:
            raise TypeError("candle should be of type -> OHCL | float | int")
        # if self.__balance() >= buy_price:
        #     self.__balance - buy_price
        #     self.__trade_book[trade_id] = []

        if trade_id in self.__trade_book.keys():
            if len(self.__trade_book.get(trade_id)) == 0:
                if self.__balance() > buy_price:
                    self.__trade_book[trade_id] = [self.__balance(), buy_price]
                    self.__balance - buy_price

            else:
                raise ReferenceError("referred trade_id is already bought.")
        else:
            raise ReferenceError("referred trade_id does not exist.")

    def sell(self, trade_id: int, candle: OHLC | float | int) -> None:
        if not isinstance(trade_id, int):
            raise TypeError("trade_id should be of type -> int")
        if isinstance(candle, OHLC):
            sell_price = SMA(1)
        elif isinstance(candle, float) or isinstance(candle, int):
            sell_price = candle
        else:
            raise TypeError("candle should be of type -> OHCL | float | int")

        if trade_id in self.__trade_book.keys():
            if len(self.__trade_book.get(trade_id)) < 3:
                self.__balance + sell_price
                self.__trade_book[trade_id].append(sell_price)
                self.__trade_book[trade_id].append(self.__balance())
            else:
                raise ReferenceError("referred trade_id is already sold.")
        else:
            raise ReferenceError("referred trade_id does not exist.")

    def trade_stats(self) -> dict:
        return self.__trade_book

