import numpy as np

def func(r,prm,cgh):
    br = prm.br
    gb = prm.gb
    br2 = br*br
    mask = np.where(r <= br, 1, 0)
    r2 = r*r
    if gb == 0:
        in_amp = mask
    elif gb == 1:
        peakAmp = np.sqrt((1*2)/(np.pi*br2))
        cgh.in_amp = peakAmp * np.exp((-2*r2)/br2)