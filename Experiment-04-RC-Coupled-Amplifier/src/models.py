import numpy as np

def rc_coupled_gain_db(frequency, A_mid, f_low, f_high):
    """
    Frequency response of single-stage RC coupled amplifier (dB).
    """
    A_mid_db = 20 * np.log10(A_mid)
    low = 1 / np.sqrt(1 + (f_low / frequency) ** 2)
    high = 1 / np.sqrt(1 + (frequency / f_high) ** 2)
    return A_mid_db + 20 * np.log10(low * high)
