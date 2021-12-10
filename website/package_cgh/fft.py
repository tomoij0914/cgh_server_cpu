import numpy as np

def foward(uh,width):
    uh_shift = np.fft.fftshift(uh)
    ur = np.fft.fft2(uh_shift) / width
    ur_shift = np.fft.fftshift(ur)
    return ur_shift

def inverse(ur,width):
    ur_shift = np.fft.ifftshift(ur)
    uh = np.fft.ifft2(ur_shift) / width
    uh_shift = np.fft.ifftshift(uh)
    return uh_shift