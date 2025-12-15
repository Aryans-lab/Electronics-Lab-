import numpy as np
from analysis import load_data, fit_cutoff, plot_bode
from models import lowpass_mag_db, highpass_mag_db

# ---------- LOW-PASS (Integrator behavior) ----------
f_lp, gain_lp = load_data("data/lowpass.csv")

fc_lp = fit_cutoff(lowpass_mag_db, f_lp, gain_lp, guess=150)
wc_lp = 2 * np.pi * fc_lp

print("LOW-PASS FILTER (Integrator)")
print(f"Cutoff frequency fc = {fc_lp:.2f} Hz")
print(f"Angular cutoff wc = {wc_lp:.2f} rad/s\n")

plot_bode(
    f_lp,
    gain_lp,
    lowpass_mag_db,
    fc_lp,
    "Active Low-Pass Filter (Integrator)"
)

# ---------- HIGH-PASS (Differentiator behavior) ----------
f_hp, gain_hp = load_data("data/highpass.csv")

fc_hp = fit_cutoff(highpass_mag_db, f_hp, gain_hp, guess=150)
wc_hp = 2 * np.pi * fc_hp

print("HIGH-PASS FILTER (Differentiator)")
print(f"Cutoff frequency fc = {fc_hp:.2f} Hz")
print(f"Angular cutoff wc = {wc_hp:.2f} rad/s")

plot_bode(
    f_hp,
    gain_hp,
    highpass_mag_db,
    fc_hp,
    "Active High-Pass Filter (Differentiator)"
)
