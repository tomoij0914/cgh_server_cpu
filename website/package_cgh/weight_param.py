def func(nor1,trg,alp):
    for kk in range(0, trg.point):
        xx = int(trg.x[kk])
        yy = int(trg.y[kk])
        tt = trg.targetI[kk]
        # weightの計算
        w = (tt/nor1[yy][xx])**alp
        # ターゲット画像の更新
        trg.target_image[yy][xx] = w * trg.target_image[yy][xx]