import numpy as np

def transfer_ratio(frequency, R, L, C):
    """
    Voltage ratio V_R / V_i for a series RLC circuit.
    """
    omega = 2 * np.pi * frequency
    impedance = np.sqrt(R**2 + (omega * L - 1 / (omega * C))**2)
    return R / impedance


def phase_angle(frequency, R, L, C):
    """
    Phase angle across the resistor (degrees).
    """
    omega = 2 * np.pi * frequency
    phi = np.arctan(R / (omega * L - 1 / (omega * C)))
    return np.degrees(phi)
