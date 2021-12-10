from django import forms

class UploadFileForm(forms.Form):
    # テキストを入力するためのフォームを生成
    #title = forms.CharField(max_length=50)

    # ファイルアップロードのためのフォームを生成
    # settings.pyにてMEDIA_ROOTを設定する必要があり
    file = forms.FileField()
