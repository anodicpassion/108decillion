from .candle import *


class SMA:
    def __init__(self, length: int = 5) -> None:
        self.__length = length
        self.__buffer = []
        self.__sma = None

    def __call__(self, candle: OHLC | float) -> float:
        if isinstance(candle, OHLC):
            value = candle.close()
        elif isinstance(candle, float):
            value = candle
        else:
            raise TypeError("candle should be of type -> OHCL or float")
        # Add the new value to the buffer
        self.__buffer.append(value)
        if len(self.__buffer) > self.__length:
            self.__buffer.pop(0)  # Remove the oldest value if buffer exceeds __length

        # Calculate SMA if enough values are present
        if len(self.__buffer) == self.__length:
            self.__sma = round(sum(self.__buffer) / self.__length, 2)
        else:
            self.__sma = None

        return self.__sma


class SmoothMA:
    def __init__(self, length):
        self.__length = length
        self.__smooth_ma = None
        self.__prev_smooth_ma = None  # To store the previous SmoothMA value
        self.__buffer = []  # To accumulate the initial values for the first SMA

    def __call__(self, candle: OHLC | float) -> float | None:
        if isinstance(candle, OHLC):
            value = candle.close()
        elif isinstance(candle, float):
            value = candle
        else:
            raise TypeError("candle should be of type -> OHCL or float")
        self.__buffer.append(value)
        if len(self.__buffer) < self.__length:
            return None  # Not enough data for the first SmoothMA
        elif len(self.__buffer) == self.__length:
            # Calculate the initial SMA
            self.__smooth_ma = np.mean(self.__buffer)
        else:
            # Calculate the SmoothMA dynamically
            self.__smooth_ma = (self.__prev_smooth_ma * (self.__length - 1) + value) / self.__length

        self.__prev_smooth_ma = self.__smooth_ma
        return round(self.__smooth_ma, 2)


class Alligator:
    def __init__(self, jaw_length=13, teeth_length=8, lips_length=5, jaw_offset=21, teeth_offset=13, lips_offset=1,
                 show_jaw=True, show_teeth=True, show_lips=True) \
            -> None:
        self.__jaw_smooth_ma = SmoothMA(jaw_length)
        self.__teeth_smooth_ma = SmoothMA(teeth_length)
        self.__lips_smooth_ma = SmoothMA(lips_length)

        self.__jaw_offset = jaw_offset
        self.__teeth_offset = teeth_offset
        self.__lips_offset = lips_offset

        self.__jaw_values = []
        self.__teeth_values = []
        self.__lips_values = []

        self.show_jaw = show_jaw
        self.show_teeth = show_teeth
        self.show_lips = show_lips

    def __call__(self, candle: OHLC) -> tuple[float, float, float] | tuple:
        if not isinstance(candle, OHLC):
            raise TypeError("candle should be of type -> OHCL")
        hl2 = (candle.high() + candle.low()) / 2
        jaw = self.__jaw_smooth_ma(hl2)
        teeth = self.__teeth_smooth_ma(hl2)
        lips = self.__lips_smooth_ma(hl2)

        self.__jaw_values.append(jaw)
        self.__teeth_values.append(teeth)
        self.__lips_values.append(lips)

        # Apply offsets (using None for uninitialized values)
        jaw_offset_value = self.__jaw_values[-self.__jaw_offset] if len(
            self.__jaw_values) >= self.__jaw_offset else None
        teeth_offset_value = self.__teeth_values[-self.__teeth_offset] if len(
            self.__teeth_values) >= self.__teeth_offset else None
        lips_offset_value = self.__lips_values[-self.__lips_offset] if len(
            self.__lips_values) >= self.__lips_offset else None

        # return {
        #     "Jaw": jaw_offset_value,
        #     "Teeth": teeth_offset_value,
        #     "Lips": lips_offset_value
        # }
        # return jaw_offset_value, teeth_offset_value, lips_offset_value
        temp = []
        if self.show_jaw:
            temp.append(jaw_offset_value)
        if self.show_teeth:
            temp.append(teeth_offset_value)
        if self.show_lips:
            temp.append(lips_offset_value)
        return tuple(temp)


class RSI:
    def __init__(self, length=14):
        self.__length = length
        self.__gains = []
        self.__losses = []
        self.__avg_gain = None
        self.__avg_loss = None
        self.__prev_value = None
        self.__rsi = None

    def __call__(self, candle: OHLC | float):
        if isinstance(candle, OHLC):
            value = candle.close()
        elif isinstance(candle, float):
            value = candle
        else:
            raise TypeError("candle should be of type -> OHCL or float")

        if self.__prev_value is None:
            # First value, we can't calculate RSI yet
            self.__prev_value = value
            return None

        # Calculate the change
        change = value - self.__prev_value
        self.__prev_value = value

        # Separate the change into gain or loss
        gain = max(change, 0)
        loss = abs(min(change, 0))

        # Store __gains and __losses
        self.__gains.append(gain)
        self.__losses.append(loss)

        if len(self.__gains) > self.__length:
            self.__gains.pop(0)
            self.__losses.pop(0)

        # Calculate average gain and loss
        if len(self.__gains) == self.__length:
            if self.__avg_gain is None and self.__avg_loss is None:
                # Initial average gain/loss (simple average)
                self.__avg_gain = sum(self.__gains) / self.__length
                self.__avg_loss = sum(self.__losses) / self.__length
            else:
                # Smoothed average (similar to EMA)
                self.__avg_gain = (self.__avg_gain * (self.__length - 1) + gain) / self.__length
                self.__avg_loss = (self.__avg_loss * (self.__length - 1) + loss) / self.__length

            # Calculate RSI
            if self.__avg_loss == 0:
                self.__rsi = 100  # RSI is 100 if there's no loss
            else:
                rs = self.__avg_gain / self.__avg_loss
                self.__rsi = 100 - (100 / (1 + rs))

        return self.__rsi


class EMA:
    def __init__(self, length):
        self.__length = length
        self.__multiplier = 2 / (length + 1)
        self.__ema = None

    def __call__(self, candle: OHLC | float) -> float:
        if isinstance(candle, OHLC):
            value = candle.close()
        elif isinstance(candle, float):
            value = candle
        else:
            raise TypeError("candle should be of type -> OHCL or float")
        if self.__ema is None:
            # Initialize EMA with the first value
            self.__ema = value
        else:
            # Calculate EMA dynamically
            self.__ema = (value - self.__ema) * self.__multiplier + self.__ema
        return round(self.__ema, 2)


class MACD:
    def __init__(self, fast_length=12, slow_length=26, signal_length=9):
        self.__fast_ema = EMA(fast_length)
        self.__slow_ema = EMA(slow_length)
        self.__signal_ema = EMA(signal_length)
        self.__macd_line = None
        self.__signal_line = None
        self.__histogram = None

    def __call__(self, candle: OHLC | float) -> tuple[float, float, float]:
        if isinstance(candle, OHLC):
            value = candle.close()
        elif isinstance(candle, float):
            value = candle
        else:
            raise TypeError("candle should be of type -> OHCL or float")
        # Update the fast and slow EMAs
        fast = self.__fast_ema(value)
        slow = self.__slow_ema(value)

        if fast is not None and slow is not None:
            # Calculate the MACD line
            self.__macd_line = fast - slow
            # Update the Signal line EMA
            self.__signal_line = self.__signal_ema(self.__macd_line)
            # Calculate the Histogram
            if self.__signal_line is not None:
                self.__histogram = self.__macd_line - self.__signal_line

        # return {
        #     "MACD_Line": self.__macd_line,
        #     "Signal_Line": self.__signal_line,
        #     "Histogram": self.__histogram
        # }
        return round(self.__macd_line, 2), round(self.__signal_line, 2), round(self.__histogram, 2)


class ATR:
    def __init__(self, length=14, smoothing="RMA"):
        self.length = length
        self.smoothing = smoothing
        self.tr_values = []  # To store True Range values
        self.atr = None
        self.prev_close = None
        # Initialize for smoothing
        if smoothing == "RMA":
            self.ma_calculator = RMA(length)
        elif smoothing == "SMA":
            self.ma_calculator = SMA(length)
        elif smoothing == "EMA":
            self.ma_calculator = EMA(length)
        elif smoothing == "WMA":
            self.ma_calculator = WMA(length)
        else:
            raise ValueError("Invalid smoothing method. Choose from RMA, SMA, EMA, WMA.")

    def __call__(self, candle: OHLC, prev_close=None) -> float | None:
        high, low, close = candle.high(), candle.low(), candle.close()

        if prev_close is not None:
            self.prev_close = prev_close

        if self.prev_close is None:
            self.prev_close = close
            return None
        # Calculate True Range (TR)
        tr = max(high - low, abs(high - self.prev_close), abs(low - self.prev_close))
        self.tr_values.append(tr)

        # Smooth the TR values using the selected method
        atr = self.ma_calculator(tr)
        self.prev_close = close
        return atr


class RMA:
    def __init__(self, length):
        self.length = length
        self.rma = None

    def __call__(self, candle: OHLC | float) -> float:
        if isinstance(candle, OHLC):
            value = candle.close()
        elif isinstance(candle, float):
            value = candle
        else:
            raise TypeError("candle should be of type -> OHCL or float")
        if self.rma is None:
            # Initialize RMA with the first value
            self.rma = value
        else:
            # Calculate RMA dynamically
            self.rma = (self.rma * (self.length - 1) + value) / self.length
        return self.rma


class WMA:
    def __init__(self, length):
        self.length = length
        self.values = []

    def __call__(self, candle: OHLC | float) -> float | None:
        if isinstance(candle, OHLC):
            value = candle.close()
        elif isinstance(candle, float):
            value = candle
        else:
            raise TypeError("candle should be of type -> OHCL or float")
        self.values.append(value)
        if len(self.values) > self.length:
            self.values.pop(0)

        if len(self.values) == self.length:
            weights = np.arange(1, self.length + 1)
            return np.dot(self.values, weights) / weights.sum()
        else:
            return None


class VolumeROC:
    def __init__(self, length: int = 14):
        self.length = length
        self.volume_buffer = []

    def __call__(self, candle: OHLC | float):
        if isinstance(candle, OHLC):
            volume = candle.volume()
        elif isinstance(candle, float):
            volume = candle
        else:
            raise TypeError("candle should be of type -> OHCL or float")

        self.volume_buffer.append(volume)

        # Ensure the buffer only keeps the last n+1 entries
        if len(self.volume_buffer) > self.length + 1:
            self.volume_buffer.pop(0)

        # Calculate VROC if we have enough data
        if len(self.volume_buffer) == self.length + 1:
            V_t = self.volume_buffer[-1]
            V_tn = self.volume_buffer[0]
            if V_tn != 0:
                vroc = ((V_t - V_tn) / V_tn) * 100
            else:
                vroc = np.nan
            return vroc
        else:
            return np.nan


class KAMA:
    def __init__(self, length=14, fast_length=2, slow_length=30, highlight=False, await_condition=True):
        """
        Initialize the Kaufman Adaptive Moving Average (KAMA) calculator.

        Parameters:
        length (int): The efficiency ratio lookback period.
        fast_length (int): The period for the fast EMA.
        slow_length (int): The period for the slow EMA.
        """
        self.length = length
        self.fast_alpha = 2 / (fast_length + 1)
        self.slow_alpha = 2 / (slow_length + 1)
        self.kama = None  # Stores the last KAMA value
        self.kama_history = []  # Stores all KAMA values for tracking
        self.price_history = []  # To store price history for calculation
        self.highlight = highlight
        self.await_condition = await_condition

    def __call__(self, candle: OHLC | float):
        if isinstance(candle, OHLC):
            price = candle.close()
        elif isinstance(candle, float):
            price = candle
        else:
            raise TypeError("candle should be of type -> OHCL")

        # Store price and ensure price history is within bounds
        self.price_history.append(price)
        if len(self.price_history) > self.length:
            self.price_history.pop(0)

        if len(self.price_history) < self.length:
            # Not enough data to compute KAMA
            if self.highlight:
                return None, 0  # Default color
            else:
                return None

        # Calculate Efficiency Ratio (ER)
        mom = abs(self.price_history[-1] - self.price_history[0])  # Momentum
        volatility = sum(abs(self.price_history[i] - self.price_history[i - 1])
                         for i in range(1, len(self.price_history)))

        er = mom / volatility if volatility != 0 else 0

        # Calculate Smoothing Constant (alpha)
        alpha = (er * (self.fast_alpha - self.slow_alpha) + self.slow_alpha) ** 2

        # Update KAMA
        if self.kama is None:
            # Initialize KAMA with the first price value
            self.kama = price
        else:
            # Dynamically update KAMA
            self.kama = alpha * price + (1 - alpha) * self.kama

        # Store KAMA value in history
        self.kama_history.append(self.kama)

        # Determine color
        if self.highlight:
            if len(self.kama_history) < 2:
                # Not enough data to determine trend
                color = 0  # Default color
            else:
                prev_kama = self.kama_history[-2]

                if self.kama > prev_kama and self.await_condition:
                    color = 1
                else:
                    color = -1
            # else:
            #     color = 0  # Default color when highlighting is off

            return self.kama, color
        else:
            return self.kama


available_indicators = [Alligator, SMA, SmoothMA, RSI, EMA, MACD]
