from analysis import load_data, fit_frequency_response, plot_response

# Load experimental data
frequency, gain_db = load_data("data/frequency_response.csv")

# Fit model
params = fit_frequency_response(frequency, gain_db)

# Plot and extract results
mid_gain_db = plot_response(frequency, gain_db, params)

A_mid, f_low, f_high = params

print("FITTED PARAMETERS")
print(f"Mid-band gain = {A_mid:.2f} ({mid_gain_db:.2f} dB)")
print(f"Lower cutoff frequency = {f_low:.1f} Hz")
print(f"Upper cutoff frequency = {f_high:.1f} Hz")
print(f"Bandwidth = {f_high - f_low:.1f} Hz")
