import numpy as np

def lowpass_mag_db(frequency, fc):
    """
    First-order active low-pass filter magnitude (dB).
    """
    return 20 * np.log10(1 / np.sqrt(1 + (frequency / fc) ** 2))


def highpass_mag_db(frequency, fc):
    """
    First-order active high-pass filter magnitude (dB).
    """
    return 20 * np.log10(1 / np.sqrt(1 + (fc / frequency) ** 2))
