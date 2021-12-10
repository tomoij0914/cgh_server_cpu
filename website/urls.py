from django.urls import path
# 同じディレクトリ（.）にあるviews.pyから，IndexViewをインポート
from . import views

urlpatterns = [
    # 終了画面
    path('finish/', views.finish, name='finish'),
    # CGHの計算
    path('run/', views.run, name='run'),
    # CGHのダウンロード
    path("download/", views.file_download, name='file_download'),
    # CSVファイルのアップロード
    path("upload_param/", views.file_upload_param, name='file_upload_param')
]

