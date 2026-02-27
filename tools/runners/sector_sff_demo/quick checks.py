# run this inside your venv, from sector_sff_demo/
import numpy as np
import json

def fit_ramp(npz, t_min=20.0, t_max=45.0):
    data = np.load(npz)
    t = data['t'].real
    K = data['K'].real
    mask = (t>=t_min) & (t<=t_max)
    a,b = np.polyfit(t[mask], K[mask], 1)  # K ≈ a*t + b
    return {'file': npz, 'slope': float(a), 'intercept': float(b)}

print(json.dumps({
    'NS_plus': fit_ramp('output/sff_NS_plus.npz'),
    'NS_minus': fit_ramp('output/sff_NS_minus.npz'),
    'R_minus': fit_ramp('output/sff_R_minus.npz'),
}, indent=2))