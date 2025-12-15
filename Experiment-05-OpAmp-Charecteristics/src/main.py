from analysis import load_data, fit_gain, plot_amplifier, plot_comparator

# ---------- Inverting Amplifier ----------
vin, vout = load_data("data/inverting.csv")
gain, intercept, r = fit_gain(vin, vout)

print("Inverting Amplifier")
print(f"Gain = {gain:.2f}, R = {r:.3f}")

plot_amplifier(
    vin, vout, gain,
    "Inverting Amplifier Characteristics"
)

# ---------- Non-Inverting Amplifier ----------
vin, vout = load_data("data/non_inverting.csv")
gain, intercept, r = fit_gain(vin, vout)

print("\nNon-Inverting Amplifier")
print(f"Gain = {gain:.2f}, R = {r:.3f}")

plot_amplifier(
    vin, vout, gain,
    "Non-Inverting Amplifier Characteristics"
)

# ---------- Comparator (Zero Threshold) ----------
vin, vout = load_data("data/comparator_basic.csv")

plot_comparator(
    vin, vout,
    "Basic Comparator Characteristic (Vth = 0 V)",
    vth=0
)

# ---------- Comparator (With Threshold) ----------
vin, vout = load_data("data/comparator_threshold.csv")

plot_comparator(
    vin, vout,
    "Comparator with Threshold Voltage",
    vth=5.02
)
