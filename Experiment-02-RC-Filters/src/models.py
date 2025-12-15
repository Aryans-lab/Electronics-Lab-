import numpy as np

def lowpass_mag(frequency, fc):
    """
    Low-pass RC magnitude (dB).
    """
    return 20 * np.log10(1 / np.sqrt(1 + (frequency / fc) ** 2))


def highpass_mag(frequency, fc):
    """
    High-pass RC magnitude (dB).
    """
    return 20 * np.log10(1 / np.sqrt(1 + (fc / frequency) ** 2))
