import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def load_data(path):
    df = pd.read_csv(path)
    return df["vin_v"].to_numpy(), df["vout_v"].to_numpy()


def fit_gain(vin, vout):
    slope, intercept, r, *_ = linregress(vin, vout)
    return slope, intercept, r


def plot_amplifier(vin, vout, gain, title):
    vin_fit = np.linspace(min(vin), max(vin), 200)
    vout_fit = gain * vin_fit

    plt.figure(figsize=(7,5))
    plt.scatter(vin, vout, s=40, label="Experimental")
    plt.plot(vin_fit, vout_fit, '--', label=f"Fit (Gain = {gain:.2f})")
    plt.xlabel("Input Voltage $V_{in}$ (V)")
    plt.ylabel("Output Voltage $V_{out}$ (V)")
    plt.title(title, weight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_comparator(vin, vout, title, vth=None):
    plt.figure(figsize=(9,5))
    plt.scatter(vin, vout, s=80, zorder=5)

    if vth is not None:
        plt.axvline(vth, ls='--', lw=2, label=f"$V_{{th}}$ = {vth:.2f} V")

    plt.axhline(0, color='k', alpha=0.3)
    plt.xlabel("Input Voltage $V_i$ (V)")
    plt.ylabel("Output Voltage $V_o$ (V)")
    plt.title(title, weight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()
