import numpy as np
from scipy.optimize import curve_fit
from models import transfer_ratio

def fit_rlc(frequency, ratio, p0):
    """
    Fit R, L, C using nonlinear least squares.
    """
    params, covariance = curve_fit(
        transfer_ratio,
        frequency,
        ratio,
        p0=p0
    )
    return params, covariance
