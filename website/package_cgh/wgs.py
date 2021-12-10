import numpy as np
from . import uniformity
from . import weight_param
from . import fft

def func(cgh,trg,prm,k,unif,best_unif):

    ###################################
    # CA on hologram plane
    cgh.uh.real = cgh.in_amp * np.cos(cgh.h_phase)
    cgh.uh.imag = cgh.in_amp * np.sin(cgh.h_phase)
    # FFT
    trg.ur = fft.foward(cgh.uh, prm.width)

    ################################
    # Intensity on Fourier plane
    r_int = np.abs(trg.ur)**2
    nor1 = r_int/np.max(r_int)

    ####################################
    # Check uniformity of reconstruction
    unif[k] = uniformity.func(nor1, trg)

    ############################################
    # Update target image
    weight_param.func(nor1, trg, prm.alp)

    ####################################
    # Phase on Fourier plane
    trg.r_phase = np.angle(trg.ur)

    ############################################
    # CA on Fourier plane
    trg.ur.real = trg.target_image * np.cos(trg.r_phase)
    trg.ur.imag = trg.target_image * np.sin(trg.r_phase)
    # IFFT
    cgh.uh = fft.inverse(trg.ur, prm.width)

    ############################################
    # Phase on hologram (CGH)w
    cgh.h_phase = np.angle(cgh.uh)

    ####################################
    print("Itr: %d" % (k + 1))
    print("Uniformity: %.2f" % unif[k])

    ####################################
    # Restore CGH
    if best_unif < unif[k]:
        best_unif = unif[k]
        cgh.saveCGH = cgh.h_phase
        trg.savePhase = trg.r_phase
        trg.saveReconst = nor1
        return [1,best_unif]
    else:
        return [0]