import numpy as np

def prandtl_circulation(x, advance_ratio, n_blades):
    # Useful variables
    lamb = advance_ratio / np.pi
    X = x/lamb
    # Tip Loss Function
    f = (n_blades /2) * ((lamb ** 2 + 1) ** 0.5 / lamb) * (1 - x)
    F = (2 / np.pi) * np.arccos(np.exp(-f))
    # Circulation Function
    K = F * X ** 2 / (X ** 2 + 1)
    return K