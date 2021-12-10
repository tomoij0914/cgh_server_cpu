import numpy as np

def func(r,trg):
    # Make phase on Fourier plane
    # random phase
    #r_phase = (2*np.pi) * np.random.rand(width, height)

    # Fresnel lens
    # pixel size (mm)
    ps = 0.020
    # focal length (mm)
    fl = 1000
    # wavelength (mm)
    ram = 0.000515
    #h_phase = np.zeros((width, height), dtype = float)
    r2 = -1*np.pi*((r*ps)**2)
    zr = fl*ram
    r_phase = np.fmod(r2/zr, 2*np.pi)
    trg.r_phase = r_phase + (-1*np.amin(r_phase))