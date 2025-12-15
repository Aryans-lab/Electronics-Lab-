import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from models import lowpass_mag_db, highpass_mag_db


def load_data(path):
    df = pd.read_csv(path)
    return df["frequency_hz"].to_numpy(), df["gain_db"].to_numpy()


def fit_cutoff(model, f, gain_db, guess=100):
    params, _ = curve_fit(
        model,
        f,
        gain_db,
        p0=[guess],
        maxfev=10000
    )
    return float(params[0])


def plot_bode(f, gain_db, model, fc, title):
    f_fit = np.logspace(np.log10(f.min()), np.log10(f.max()), 800)
    gain_fit = model(f_fit, fc)

    plt.figure(figsize=(8,6))
    plt.semilogx(f, gain_db, 'o', label="Experimental")
    plt.semilogx(f_fit, gain_fit, 'r', lw=2,
                 label=f"Fit (fc ≈ {fc:.1f} Hz)")

    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Gain |H(jω)| (dB)")
    plt.title(title, weight='bold')
    plt.grid(True, which="both", ls="--", lw=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()
