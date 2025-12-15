# Experiment 01: Frequency Response of a Series LCR Circuit

## Objective
To study the frequency dependence of voltage ratio and phase in a series LCR circuit
and extract R, L, and C via nonlinear fitting.

## Theory
For a series RLC circuit driven by a sinusoidal source:

|Z| = sqrt[R² + (ωL − 1/ωC)²]

Voltage ratio:
V_R / V_i = R / |Z|

Phase:
φ = arctan[R / (ωL − 1/ωC)]

## Methodology
- Experimental data recorded for two resistances
- Nonlinear least squares fitting using SciPy
- Comparison of experimental and theoretical curves

## Results
Fitted parameters show good agreement with nominal component values.

## Tools
- Python
- NumPy
- SciPy
- Matplotlib
