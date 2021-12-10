def func(nor_int, trg):
    point = trg.point
    x = trg.x
    y = trg.y
    targ = trg.targetI

    max_peak = 0
    min_peak = 1
    for k in range(0, point):
        xx = int(x[k])
        yy = int(y[k])
        peak = nor_int[yy][xx] / targ[k]
        if peak < min_peak:
            min_peak = peak
        if max_peak < peak:
            max_peak = peak
    unif = min_peak/max_peak
    return unif