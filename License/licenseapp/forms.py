from django import forms
from .models import License

# ModelFormを継承したフォームクラス
class LicenseForm(forms.ModelForm):
    """ 新規データ登録画面用のフォーム定義 """
    class Meta:
        model = License
        fields = ['date', 'category', 'company',
                  'language', 'money', 'comment',]
