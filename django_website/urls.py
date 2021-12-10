from django.urls import path, include
# 画像の表示に必要
from . import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    # トップページにアクセスしたらwebsiteアプリフォルダのurls.pyに移動
    path('', include("website.urls")),
]
# 画像の表示に必要,MEDIA_URLとMEDIA_ROOTを設定
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
