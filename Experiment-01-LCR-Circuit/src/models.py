import numpy as np

def transfer_ratio(f, R, L, C):
    """
    Voltage ratio V_R / V_i for a series RLC circuit.
    """
    omega = 2 * np.pi * f
    Z = np.sqrt(R**2 + (omega*L - 1/(omega*C))**2)
    return R / Z

def phase_angle(f, R, L, C):
    """
    Phase angle across resistor (degrees).
    """
    omega = 2 * np.pi * f
    phi = np.arctan(R / (omega*L - 1/(omega*C)))
    return np.degrees(phi)
