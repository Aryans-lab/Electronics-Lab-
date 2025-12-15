import pandas as pd
from analysis import (
    load_input,
    fit_input,
    plot_input,
    plot_output,
    plot_transfer
)

# ---------- Input characteristics ----------
V1, I1 = load_input("data/input_vce_0p2.csv")
V2, I2 = load_input("data/input_vce_1p0.csv")

p1 = fit_input(V1, I1)
p2 = fit_input(V2, I2)

plot_input(V1, I1, p1, "Input Characteristics (VCE = 0.2 V)")
plot_input(V2, I2, p2, "Input Characteristics (VCE = 1.0 V)")

# ---------- Output characteristics ----------
df_out = pd.read_csv("data/output_curves.csv")
plot_output(df_out)

# ---------- Transfer characteristics ----------
plot_transfer("data/transfer.csv")
