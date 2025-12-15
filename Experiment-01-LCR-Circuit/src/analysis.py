import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

from models import transfer_ratio, phase_angle


def load_table_1(path):
    df = pd.read_csv(path)
    return (
        df["frequency_hz"].to_numpy(),
        df["vr_vi"].to_numpy(),
        df["phase_deg"].to_numpy()
    )


def load_table_2(path):
    df = pd.read_csv(path)
    return (
        df["frequency_hz"].to_numpy(),
        df["vr_vi"].to_numpy()
    )


def load_table_3(path):
    df = pd.read_csv(path)
    return (
        df["frequency_hz"].to_numpy(),
        df["vlc_vi"].to_numpy(),
        df["phase_deg"].to_numpy()
    )


def fit_rlc(frequency, ratio, initial_guess):
    params, covariance = curve_fit(
        transfer_ratio,
        frequency,
        ratio,
        p0=initial_guess
    )
    return params, covariance


def plot_magnitude(f, ratio_exp, params, title, ylabel):
    f_fit = np.linspace(f.min(), f.max(), 800)
    ratio_fit = transfer_ratio(f_fit, *params)

    plt.figure(figsize=(9, 5))
    plt.scatter(f / 1e3, ratio_exp, s=30, label="Experimental")
    plt.plot(f_fit / 1e3, ratio_fit, 'r', label="Fit")
    plt.xlabel("Frequency (kHz)")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_phase(f, phase_exp, params, title):
    f_fit = np.linspace(f.min(), f.max(), 800)
    phase_fit = phase_angle(f_fit, *params)

    plt.figure(figsize=(9, 5))
    plt.scatter(f / 1e3, phase_exp, s=30, label="Experimental")
    plt.plot(f_fit / 1e3, phase_fit, 'r', label="Fit")
    plt.xlabel("Frequency (kHz)")
    plt.ylabel("Phase (deg)")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()
