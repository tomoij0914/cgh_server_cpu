import numpy as np
import csv

def cgh(fp,infilename,path):
    # 文字列から'target'を削除
    outfilename = path + '/website/saved_cgh/cgh_%s.bmp' %infilename
    fp.save(outfilename)

def cgh_server(fp,infilename,path):
    outfilename = path + '/media/documents/cgh_%s.bmp' %infilename
    fp.save(outfilename)

def reconst(fp,infilename,path):
    outfilename = path + '/website/result/reconst_%s.bmp' %infilename
    fp.save(outfilename)

def target(fp,infilename,path):
    fp.save(path + '/website/target/' + 'target_' + infilename + '.bmp')

def raw(saveReconst,infilename,path):
    outfilename = path + "/website/result/recons_%s.npy" % infilename
    np.save(outfilename, saveReconst)

def csvfile(hdx, hdy, x, y, k, infilename, path, chr):
    str = path + "/website/result/" + chr + "_%s.csv" % infilename
    # ヘッダー
    header = [hdx,hdy]
    # ファイルを書き込みモードでオープン
    with open(str, 'w', newline="") as f:
        writer = csv.writer(f,lineterminator='\n')
        writer.writerow(header)
        for i in range(k):
            data = [x[i],y[i]]
            writer.writerow(data)