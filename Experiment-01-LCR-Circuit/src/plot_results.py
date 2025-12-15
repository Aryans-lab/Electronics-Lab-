import numpy as np
import matplotlib.pyplot as plt
from models import transfer_ratio, phase_angle

def plot_magnitude(f, ratio_exp, params, title, label):
    f_fit = np.linspace(f.min(), f.max(), 800)
    ratio_fit = transfer_ratio(f_fit, *params)

    plt.figure(figsize=(9,5))
    plt.scatter(f/1e3, ratio_exp, s=25, label="Experimental")
    plt.plot(f_fit/1e3, ratio_fit, 'r', label="Fit")
    plt.xlabel("Frequency (kHz)")
    plt.ylabel("V_R / V_i")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_phase(f, phi_exp, params, title):
    f_fit = np.linspace(f.min(), f.max(), 800)
    phi_fit = phase_angle(f_fit, *params)

    plt.figure(figsize=(9,5))
    plt.scatter(f/1e3, phi_exp, s=25, label="Experimental")
    plt.plot(f_fit/1e3, phi_fit, 'r', label="Fit")
    plt.xlabel("Frequency (kHz)")
    plt.ylabel("Phase (deg)")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()
