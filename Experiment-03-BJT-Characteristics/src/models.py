import numpy as np

def diode_like(V, a, b, c):
    """
    Exponential model for B-E junction.
    """
    return a * np.exp(b * V) + c
