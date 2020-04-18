from django import forms
from .models import *


# 新規データ登録画面用のフォーム定義
class LicenseForm(forms.ModelForm):
    class Meta:
        model = T_License
        fields = [
            'company', 'language', 'application', 'display_number', 'hid',
            'remaining_point', 'memo'
        ]


#################################################
class ParentForm(forms.ModelForm):
    class Meta:
        model = T_License
        fields = [
            'company', 'language', 'application', 'display_number', 'hid',
            'remaining_point', 'memo'
        ]

    def save(self, commit=True):
        instance = super(ParentForm, self).save(commit=commit)
        if commit:
            instance.save()
        return instance
