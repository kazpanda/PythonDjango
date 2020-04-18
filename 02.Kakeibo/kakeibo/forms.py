from django import forms
from .models import Kakeibo


class KakeiboForm(forms.ModelForm):
    """
    新規データ登録画面用のフォーム定義
    """
    class Meta:
        model = Kakeibo
        fields =['date', 'category', 'license', 'money', 'memo']