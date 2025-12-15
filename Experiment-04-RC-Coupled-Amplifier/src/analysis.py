import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from models import rc_coupled_gain_db


def load_data(path):
    df = pd.read_csv(path)
    f = df["frequency_hz"].to_numpy()
    gain = df["gain"].to_numpy()
    gain_db = 20 * np.log10(gain)
    return f, gain_db


def fit_frequency_response(f, gain_db):
    A_mid_guess = 10 ** (np.max(gain_db) / 20)
    p0 = [A_mid_guess, 10, 1e5]

    params, _ = curve_fit(
        rc_coupled_gain_db,
        f,
        gain_db,
        p0=p0,
        bounds=([0.1, 1, 1e3], [20, 1e4, 1e7]),
        maxfev=20000
    )
    return params


def plot_response(f, gain_db, params):
    A_mid, f_low, f_high = params
    mid_gain_db = 20 * np.log10(A_mid)

    f_fit = np.logspace(np.log10(f.min()), np.log10(f.max()), 1200)
    gain_fit = rc_coupled_gain_db(f_fit, *params)

    plt.figure(figsize=(10,6))
    plt.semilogx(f, gain_db, 'o', label="Measured")
    plt.semilogx(f_fit, gain_fit, 'r', lw=2.5, label="Fit")

    plt.axhline(mid_gain_db, ls='--', label=f"Mid-band = {mid_gain_db:.2f} dB")
    plt.axhline(mid_gain_db - 3, ls='--', label="-3 dB")
    plt.axvline(f_low, ls=':', label=f"f_L = {f_low:.0f} Hz")
    plt.axvline(f_high, ls=':', label=f"f_H = {f_high/1000:.1f} kHz")

    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Gain (dB)")
    plt.title("RC Coupled Amplifier Frequency Response", weight='bold')
    plt.grid(True, which="both", alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()

    return mid_gain_db
