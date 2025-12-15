from analysis import (
    load_data,
    fit_cutoff,
    find_3db,
    plot_bode_magnitude,
    plot_phase
)
from models import lowpass_mag, highpass_mag
import numpy as np

# ---------------- LOW-PASS FILTER ----------------

f_lp, mag_lp, phi_lp = load_data("data/lowpass.csv")

fc_lp = fit_cutoff(lowpass_mag, f_lp, mag_lp)
wc_lp = 2 * np.pi * fc_lp
f3_lp = find_3db(lowpass_mag, fc_lp, f_lp.min(), f_lp.max())

print("LOW-PASS FILTER")
print(f"fc (fit) = {fc_lp:.2f} Hz")
print(f"wc       = {wc_lp:.2f} rad/s")
print(f"fc (-3 dB) = {f3_lp:.2f} Hz\n")

plot_bode_magnitude(
    f_lp, mag_lp, lowpass_mag, fc_lp,
    "RC Low-pass Filter — Bode Magnitude"
)

plot_phase(
    f_lp, phi_lp,
    "RC Low-pass Filter — Phase Response"
)

# ---------------- HIGH-PASS FILTER ----------------

f_hp, mag_hp, phi_hp = load_data("data/highpass.csv")

fc_hp = fit_cutoff(highpass_mag, f_hp, mag_hp)
wc_hp = 2 * np.pi * fc_hp
f3_hp = find_3db(highpass_mag, fc_hp, f_hp.min(), f_hp.max())

print("HIGH-PASS FILTER")
print(f"fc (fit) = {fc_hp:.2f} Hz")
print(f"wc       = {wc_hp:.2f} rad/s")
print(f"fc (-3 dB) = {f3_hp:.2f} Hz")

plot_bode_magnitude(
    f_hp, mag_hp, highpass_mag, fc_hp,
    "RC High-pass Filter — Bode Magnitude"
)

plot_phase(
    f_hp, phi_hp,
    "RC High-pass Filter — Phase Response"
)
