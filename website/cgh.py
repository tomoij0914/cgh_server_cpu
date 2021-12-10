# Normal code (.py)
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
import time
import os

############################################
# Road package
from .package_cgh import *

##########################################################
def func(param_fname, path):
    ########################################################
    # make class
    class ParamInfo:
        pass
    prm = ParamInfo()

    class CghInfo:
        pass
    cgh = CghInfo()

    class TargetInfo:
        pass
    trg = TargetInfo()

    ############################################
    # Read Setting parameter
    read_parameter.func(param_fname,path,prm,trg,cgh)

    ########################################
    # uniformity
    unif = np.zeros((prm.itr), dtype=float)

    ########################################
    # polor cordinate
    ilist = np.array([[i for i in range(prm.width)] for j in range(prm.height)], dtype=int)
    jlist = np.array([[j for i in range(prm.width)] for j in range(prm.height)], dtype=int)
    r = np.sqrt((prm.hh - jlist) ** 2 + (prm.hw - ilist) ** 2)

    ###########################################################
    # Make amplitude on hologram plane
    make_gaussian_beam.func(r,prm,cgh)

    ###########################################################
    # Make phase on Fourier plane
    make_fourier_phase.func(r,trg)

    #######################################################
    # CA on Fourier plane
    trg.ur.real = trg.target_image * np.cos(trg.r_phase)
    trg.ur.imag = trg.target_image * np.sin(trg.r_phase)
    # IFFT
    cgh.uh = fft.inverse(trg.ur, prm.width)

    #################################
    # Phase on hologram (CGH)
    cgh.h_phase = np.angle(cgh.uh)

    ###########################################################
    # WGS algorithm
    best_unif = 0.0
    start_time = time.perf_counter()
    for k in range(prm.itr):
        buff = wgs.func(cgh,trg,prm,k,unif,best_unif)
        if buff[0] == 1:
            best_unif = buff[1]

    ############################################
    calc_time = time.perf_counter() - start_time
    print("Toal time for calculation: {:.3f} sec".format(time.perf_counter() - start_time), flush=True)
    print("Best uniformity: %.2f" %best_unif,flush=True)

    #######################################################
    # save best CGH
    nor8_cgh = np.uint8(np.around(((cgh.saveCGH / (2*np.pi))*255)))
    fp = Image.fromarray(nor8_cgh)
    save.cgh(fp, prm.infilename, path)
    # serverへのCGHの保存
    save.cgh_server(fp, prm.infilename, path)

    ########################################################
    # Save best reconstruction
    nor8_int = np.uint8(np.around(trg.saveReconst*255))
    fp = Image.fromarray(nor8_int)
    # image crop
    ww = prm.width - prm.crop_size
    hh = prm.height - prm.crop_size
    fp_crop = fp.crop((ww/2, hh/2, prm.crop_size+ww/2, prm.crop_size+hh/2))
    save.reconst(fp_crop, prm.infilename, path)

    ################################
    # Reconstruction(raw)の保存
    save.raw(trg.saveReconst, prm.infilename, path)

    #################################
    # show best profile of reconstruction
    if prm.x_prof == 0:
        yprofi = trg.saveReconst[prm.y_prof, :]
    elif prm.y_prof == 0:
        yprofi = trg.saveReconst[:, prm.x_prof]
    xprofi = np.array([i for i in range(prm.width)], dtype=int)
    # save profile
    str = 'profile'
    save.csvfile("width","intensity",xprofi, yprofi, len(xprofi), prm.infilename, path, str)

    #################################
    # show uniformity
    xunif = np.array([i + 1 for i in range(prm.itr)], dtype=int)
    # save uniformity
    str = 'uniformity'
    save.csvfile("itr","uniformity",xunif, unif, len(unif), prm.infilename, path, str)
    
    ################################
    return [prm.infilename, prm.itr, best_unif, calc_time]
    print("Finish\n", flush=True)