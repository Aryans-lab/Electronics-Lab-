import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import linregress

from models import diode_like


def load_input(path):
    df = pd.read_csv(path)
    return df["VEB_V"].to_numpy(), df["IB_uA"].to_numpy()


def fit_input(V, I):
    mask = I > 0
    params, _ = curve_fit(diode_like, V[mask], I[mask], p0=[1e-3, 20, 0])
    return params


def plot_input(V, I, params, title):
    V_fit = np.linspace(V.min(), V.max(), 400)
    I_fit = diode_like(V_fit, *params)

    plt.figure(figsize=(7,5))
    plt.scatter(V, I, s=20)
    plt.plot(V_fit, I_fit, '--')
    plt.xlabel(r"$V_{EB}$ (V)")
    plt.ylabel(r"$I_B$ ($\mu A$)")
    plt.title(title, weight='bold')
    plt.grid(True, ls='--', lw=0.5)
    plt.tight_layout()
    plt.show()


def plot_output(df, VCC=30, RC=990):
    plt.figure(figsize=(10,6))

    for ib in sorted(df.IB_uA.unique()):
        sub = df[df.IB_uA == ib]
        plt.plot(sub.VCE_V, sub.IC_mA, marker='o', label=f"$I_B$={ib} µA")

    V = np.linspace(0, VCC, 300)
    I = (VCC - V) / RC * 1000
    plt.plot(V, I, 'r--', label="Load line")

    plt.xlabel("$V_{CE}$ (V)")
    plt.ylabel("$I_C$ (mA)")
    plt.title("Output Characteristics with Load Line", weight='bold')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_transfer(path):
    df = pd.read_csv(path)
    slope, intercept, *_ = linregress(df.IB_uA, df.IC_mA)

    IB_fit = np.linspace(0, 45, 200)
    IC_fit = slope * IB_fit + intercept

    plt.figure(figsize=(7,5))
    plt.scatter(df.IB_uA, df.IC_mA)
    plt.plot(IB_fit, IC_fit, '--')
    plt.xlabel(r"$I_B$ ($\mu A$)")
    plt.ylabel(r"$I_C$ (mA)")
    plt.title("Transfer Characteristics", weight='bold')
    plt.text(10, 5.5, f"$\\beta_{{ac}}$ = {slope*1000:.1f}")
    plt.grid(True, ls='--', lw=0.5)
    plt.show()
