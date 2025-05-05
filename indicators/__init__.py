import numpy as np
import pandas as pd
import datetime, time


def time_to_epoch(date):
    date_obj = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    epoch_time = int(time.mktime(date_obj.timetuple()))
    return epoch_time


def epoch_to_time(epoch):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch))


def vroc(volume_data, n):
    """
    Calculate the Volume Rate of Change (VROC)

    Parameters:
    volume_data (list or array-like): A list or array of volume data, with the most recent volume at the end.
    n (int): The number of periods over which to calculate the VROC.

    Returns:
    float: The Volume Rate of Change (VROC) value.
    """
    if len(volume_data) < n + 1:
        return np.nan

    V_t = volume_data[-1]

    V_tn = volume_data[-n - 1]

    vroc = ((V_t - V_tn) / V_tn) * 100

    return vroc


def sma(source, length):
    cumsum = np.cumsum(np.insert(source, 0, 0))
    sma_values = (cumsum[length:] - cumsum[:-length]) / length
    sma_values = np.concatenate((np.full(length - 1, np.nan), sma_values))
    return sma_values


def smma(data, length):
    """
    Calculate the Smoothed Moving Average (SMMA) using NumPy.

    Parameters:
    data (pd.Series or np.ndarray): The input data (like closing prices or hl2).
    __length (int): The __length of the SMMA window.

    Returns:
    np.ndarray: SMMA values as a NumPy array.
    """
    smma = np.zeros_like(data)
    smma[length - 1] = np.mean(data[:length])  # Initial SMA value
    for i in range(length, len(data)):
        smma[i] = (smma[i - 1] * (length - 1) + data[i]) / length
    return smma


# Alligator Indicator function
def alligator(data, jaw_length=13, teeth_length=8, lips_length=5, jaw_offset=21, teeth_offset=13,
              lips_offset=1):
    """
    Calculate the Williams Alligator Indicator using NumPy for efficiency.

    Parameters:
    data (pd.Series or np.ndarray): Input price data (like hl2).
    jaw_length (int): Length for the Jaw SMMA.
    teeth_length (int): Length for the Teeth SMMA.
    lips_length (int): Length for the Lips SMMA.
    __jaw_offset (int): Offset for the Jaw line.
    __teeth_offset (int): Offset for the Teeth line.
    __lips_offset (int): Offset for the Lips line.

    Returns:
    pd.DataFrame: A dataframe with Jaw, Teeth, and Lips values.
    """
    data = np.array(data)  # Ensure the data is in NumPy array format

    # Calculate SMMA for Jaw, Teeth, and Lips
    jaw = smma(data, jaw_length)
    teeth = smma(data, teeth_length)
    lips = smma(data, lips_length)

    # Apply the offsets using NumPy's shift mechanism
    jaw_shifted = np.roll(jaw, jaw_offset)
    teeth_shifted = np.roll(teeth, teeth_offset)
    lips_shifted = np.roll(lips, lips_offset)

    # For the rolled values, set the first few entries as NaN (due to shifting)
    jaw_shifted[:jaw_offset] = np.nan
    teeth_shifted[:teeth_offset] = np.nan
    lips_shifted[:lips_offset] = np.nan

    # Combine into a DataFrame
    alligator_df = pd.DataFrame({
        'Jaw': jaw_shifted,
        'Teeth': teeth_shifted,
        'Lips': lips_shifted
    })

    return alligator_df
