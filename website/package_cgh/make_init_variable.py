import numpy as np

def func(prm,trg,cgh):
    # Initialize array for CGH calculation
    cgh.uh = np.zeros((prm.width, prm.height), dtype=complex)
    trg.imageIn_bmp = np.zeros((prm.width, prm.height), dtype=int)
    trg.target_image = np.zeros((prm.width, prm.height), dtype=float)
    trg.ur = np.zeros((prm.width, prm.height), dtype=complex)
    trg.x = np.zeros(trg.point, dtype=int)
    trg.y = np.zeros(trg.point, dtype=int)
    trg.targetI = np.zeros(trg.point, dtype=float)