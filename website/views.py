# Djangoの標準view, htmlをそのままユーザーに返す
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import FileResponse
import os
from .forms import UploadFileForm
import sys
import csv
import numpy as np
from PIL import Image
from . import cgh
from django.http import HttpResponse
from django.shortcuts import redirect

#########################################################
# # manage.pyのファイルディレクトリ
path = "/home/bigvalley/bigvalley.pythonanywhere.com"
#path = os.getcwd()

#########################
# ------------------------------------------------------------------
# request: ブラウザからのリクエスト（HttpRequestクラスのオブジェクト）
def file_upload_param(request):
    global param_file_name
    # POSTメソッド：データの提供
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            file_obj = request.FILES['file']
            param_file_name = file_obj
            template_name = "cgh_calculation.html"

            # Read setting parameter
            param, point = read_set_param()

            context = {
                'fname': file_obj.name,
                'number_diffraction_point': point,
                'size_cgh': param[0][1],
                'type_input_beam': param[1][1],
                'beam_radius_input_beam': param[2][1],
                'number_iteration': param[3][1],
                'alpha_wgs': param[4][1],
                'trg_name': 'target_thumbnail.bmp'
            }
            return render(request, template_name, context)

    # GETメソッド：ページの表示を要求
    elif request.method == 'GET':
        param = UploadFileForm()
        template_name = "upload_param.html"
        return render(request, template_name, {'form': param})

# ------------------------------------------------------------------
# ファイルアップロード関数
def handle_uploaded_file(file_obj):
    dir = path + '/media/documents/' + file_obj.name
    with open(dir, 'wb') as destination:
        for chunk in file_obj.chunks():
            destination.write(chunk)

#########################
# ファイルダウンロード関数
def file_download(request):
    global cgh_file_name
    dir = path + '/website/saved_cgh/' + cgh_file_name
    # ファイルの保存
    return FileResponse(open(dir, "rb"), as_attachment=True, filename=cgh_file_name)

#########################
# 計算終了の表示
def finish(request):
    template_name = "finish.html"
    return render(request, template_name)

#########################
# CGH設計の開始
def run(request):
    global param_file_name
    global cgh_file_name

    #########################################################
    # CGHの計算
    buff = cgh.func(str(param_file_name), path)
    cgh_file_name = "cgh_%s.bmp" % buff[0]
    # 計算終了にhtmlを表示
    template_name = "finish.html"
    params = {
        # 小数点の桁数を指定
        'cgh_name': cgh_file_name,
        'iteration': f'{buff[1]:.0f}',
        'best_unif': f'{buff[2]:.2f}',
        'calc_time': f'{buff[3]:.1f}'
    }
    return render(request, template_name, params)

#########################
def read_set_param():
    # ファイルをオープン
    dir = path + '/media/documents/'+str(param_file_name)
    f = open(dir, 'r')
    # 行数の取得
    count = 0
    for line in f:
        count += 1
    # 回折点の数
    point = count - 10

    #####################################
    # 2次元リストの定義
    param = [[] for i in range(count)]

    #####################################
    # ファイルをオープン
    f = open(dir, 'r')
    # ファイルからデータを読み込み
    rows = csv.reader(f)
    j = 0
    # for文で行を1つずつ取り出す
    for row in rows:
        param[j] = row
        j += 1

    ######################################################
    bmp = np.zeros((int(param[0][1]), int(param[0][1])), dtype=int)
    for k in range (point):
        x = int(param[10+k][0])
        y = int(param[10+k][1])
        intensity = float(param[10+k][2])
        bmp[y][x] = int(intensity*255)

    # Target imageのBMPファイルの保存
    nor8_int = np.uint8(bmp)
    fp = Image.fromarray(nor8_int)
    # image crop
    ww = int(param[0][1]) - int(param[0][1])*3/5
    hh = int(param[0][1]) - int(param[0][1])*3/5
    fp_crop = fp.crop((ww, hh, int(param[0][1])/5+ww, int(param[0][1])/5+hh))
    fp_crop.save(path + '/media/documents/' + 'target_thumbnail.bmp')

    return param,point


