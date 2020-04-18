from django import forms
from .models import Post, T_Publication, T_Operation


# --------------------------------------------
# ライセンス作成フォーム
# --------------------------------------------
class NewOperationForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is in your mind?'}
        ),
        max_length=100,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = T_Operation
        fields = ['starting_count', 'weekly_report_count',
                  'monthly_report_count', 'memo'
                  ]


# --------------------------------------------
# ライセンス作成フォーム
# --------------------------------------------
class NewPublicationForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is in your mind?'}
        ),
        max_length=100,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = T_Publication
        fields = ['mac_address', 'price', 'grant_points',
                  'remaining_point', 'renewal_deadline_notification',
                  'renewal_application_accepted', 'renewal_application_send',
                  'renewal_key_publish_notification',
                  'discontinued_product_collection', 'memo'
                  ]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]
