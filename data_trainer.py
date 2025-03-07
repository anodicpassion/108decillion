import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, Reshape, Input, Flatten
from sklearn.model_selection import train_test_split

data = pd.read_csv('data/zeel/NSwE-ZEEL-EQ_2.csv')

data = data.to_numpy()
data = data[:, 1:]

X, y = [], []
last_candles_count = 8
next_candles_count = 3

for idx, row in enumerate(data[last_candles_count - 1:-(next_candles_count + 1)]):
    idx = idx + last_candles_count + 1
    first_open = data[idx - last_candles_count - 1][0]
    first_jaw = data[idx - last_candles_count - 1][4]
    first_lip = data[idx - last_candles_count - 1][6]
    first_teeth = data[idx - last_candles_count - 1][5]
    first_ma5 = data[idx - last_candles_count - 1][7]
    first_ma15 = data[idx - last_candles_count - 1][8]
    first_volumn_change = data[idx - last_candles_count - 1][9]
    last_candles = []
    for candle in data[idx - last_candles_count: idx]:
        temp = []
        temp.append(round(candle[0] - first_open, 2))
        temp.append(round(candle[1] - first_open, 2))
        temp.append(round(candle[2] - first_open, 2))
        temp.append(round(candle[3] - first_open, 2))
        temp.append(round(candle[4] - first_jaw, 2))
        temp.append(round(candle[5] - first_teeth, 2))
        temp.append(round(candle[6] - first_lip, 2))
        temp.append(round(candle[7] - first_ma5, 2))
        temp.append(round(candle[8] - first_ma15, 2))
        temp.append(round(candle[9] - first_volumn_change, 2))

        last_candles.append(temp)
    X.append(last_candles)
    next_candles = []
    for candle in data[idx: idx + next_candles_count]:
        temp = []
        temp.append(round(candle[0] - first_open, 2))

        next_candles.append(temp[0])
    y.append(next_candles)

print("data:\n", data[:8])
print("-1 data:\n", data[-1])
print("\nX:", X[0])
print("\ny:", y[0])
print("X.shape:", np.array(X).shape, "y.shape:", np.array(y).shape)

X = tf.constant(X, dtype=tf.float32)
y = tf.constant(y, dtype=tf.float32)
X_train, X_test, y_train, y_test = train_test_split(X.numpy(), y.numpy(), test_size=0.05, random_state=42)

model = Sequential()
model.add(Input(shape=(last_candles_count, 10)))
model.add(LSTM(200, activation='tanh', return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(150, activation='tanh'))
model.add(Dropout(0.2))
model.add(Dense(next_candles_count))
# model.add(Reshape((3, 11)))
model.compile(optimizer='adam', loss='mse')

history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2)

model.save("08OCT.keras")