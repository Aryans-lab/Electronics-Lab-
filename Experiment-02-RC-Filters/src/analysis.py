import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.optimize import brentq

from models import lowpass_mag, highpass_mag


def load_data(path):
    df = pd.read_csv(path)
    return (
        df["frequency_hz"].to_numpy(),
        df["magnitude_db"].to_numpy(),
        df["phase_deg"].to_numpy()
    )


def fit_cutoff(model, frequency, magnitude, p0=300):
    params, _ = curve_fit(model, frequency, magnitude, p0=[p0], maxfev=10000)
    return float(params[0])


def find_3db(model, fc, fmin, fmax):
    target = -3.0
    try:
        return brentq(lambda f: model(f, fc) - target, fmin, fmax)
    except Exception:
        return np.nan


def set_semilog_ticks(ax):
    ax.set_xscale("log")
    ticks = [20,30,40,60,80,100,200,300,400,500,700,1000,1500,2000]
    ax.set_xticks(ticks)
    ax.get_xaxis().set_major_formatter(plt.ScalarFormatter())
    ax.ticklabel_format(style="plain", axis="x")
    ax.grid(which="both", ls="--", lw=0.5, alpha=0.7)


def plot_bode_magnitude(f, mag, model, fc, title):
    f_fit = np.logspace(np.log10(f.min()), np.log10(f.max()), 1000)

    fig, ax = plt.subplots(figsize=(9,5))
    ax.semilogx(f, mag, 'o', label="Measured", markeredgecolor='k')
    ax.semilogx(f_fit, model(f_fit, fc), lw=2.5, label=f"Fit (fc={fc:.1f} Hz)")
    ax.axvline(fc, color='r', ls='--', lw=1.2)

    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("|H(jω)| (dB)")
    ax.set_title(title, weight='bold')
    set_semilog_ticks(ax)
    ax.legend()
    plt.tight_layout()
    plt.show()


def plot_phase(f, phase, title):
    fig, ax = plt.subplots(figsize=(9,4))
    ax.semilogx(f, phase, 'o', markeredgecolor='k')
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Phase (deg)")
    ax.set_title(title, weight='bold')
    set_semilog_ticks(ax)
    plt.tight_layout()
    plt.show()
