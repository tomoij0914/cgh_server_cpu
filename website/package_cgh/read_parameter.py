import csv
import numpy as np
from PIL import Image
import os
import shutil
from . import save
from . import make_init_variable

def func(param_fname,path,prm,trg,cgh):
    ##################################################
    #Read setting parameter (.csv)
    dir = path + '/media/documents/' + param_fname
    # copy csv file
    copy_dir = path + '/website/parameter'
    shutil.copy(dir, copy_dir)

    #####################################
    # ファイルをオープン
    f = open(dir, 'r')
    # 行数の取得
    count = 0
    for line in f:
        count += 1
    # 回折点の数
    trg.point = count - 10

    #####################################
    # 2次元リストの定義
    buf = [[] for i in range(count)]

    #####################################
    # ファイルをオープン
    f = open(dir, 'r')
    # ファイルからデータを読み込み
    rows = csv.reader(f)
    j = 0
    # for文で行を1つずつ取り出す
    for row in rows:
        buf[j] = row
        j += 1

    ##################################################
    prm.width = int(buf[0][1])
    prm.height = int(buf[0][1])
    prm.hw = int(prm.width/2)
    prm.hh = int(prm.height/2)
    print("Size of CGH (pixel): %d" %prm.width)

    #####################################################
    prm.gb = int(buf[1][1])
    if prm.gb==0:
        print("Type of input beam: Flat top")
    elif prm.gb==1:
        print("Type of input beam: Gaussian")

    #####################################################
    prm.br = int(buf[2][1])
    print("Beam radius (pixel): %d" %prm.br)

    #####################################################
    prm.itr = int(buf[3][1])
    print("Number of iteration: %d" %prm.itr)

    #####################################################
    prm.alp = float(buf[4][1])
    print("Alpha of WGS: %.2f" %prm.alp)

    #####################################################
    prm.crop_size = int(buf[5][1])
    print("Size of cropped image (pixel): %d" %prm.crop_size)
    prm.gxd = prm.crop_size/5
    prm.gyd = prm.crop_size/5
    prm.hcs = int(prm.crop_size/2)

    #####################################################
    prm.x_prof = int(buf[6][1])
    prm.y_prof = int(buf[7][1])
    print("Coordinate of intensity profile (pixel): (x,y)= (%d,%d)" %(prm.x_prof,prm.y_prof))

    #####################################################
    prm.infilename = buf[8][1]
    print("Saved file name (.bmp): %s" %prm.infilename)
    print("Number of diffraction beam: %d\n" % trg.point)

    #####################################################
    # 初期変数の作成
    make_init_variable.func(prm,trg,cgh)

    ######################################################
    for k in range (trg.point):
        trg.x[k] = int(buf[10+k][0])
        trg.y[k] = int(buf[10+k][1])
        trg.targetI[k] = float(buf[10+k][2])
        ##################################################
        xx = trg.x[k]
        yy = trg.y[k]
        vv = trg.targetI[k]
        trg.target_image[yy][xx] = vv
        trg.imageIn_bmp[yy][xx] = int(vv*255)

    # Target imageのBMPファイルの保存
    nor8_int = np.uint8(trg.imageIn_bmp)
    fp = Image.fromarray(nor8_int)
    save.target(fp,prm.infilename,path)

    #####################################################
    f.close()