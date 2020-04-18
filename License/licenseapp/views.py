from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import License, Category, Company
from .forms import LicenseForm
from django.urls import reverse_lazy


#一覧表示用のDjango標準ビュー(ListView)を承継して一覧表示用のクラスを定義
class LicenseListView(ListView):
    #利用するモデルを指定
    model = License
    #データを渡すテンプレートファイルを指定
    template_name = 'licenseapp/license_list.html'

    #家計簿テーブルの全データを取得するメソッドを定義
    def queryset(self):
        return License.objects.all()


class LicenseCreateView(CreateView):
    #利用するモデルを指定
    model = License
    #利用するフォームクラス名を指定
    form_class = LicenseForm
    #登録処理が正常終了した場合の遷移先を指定(空間名:パターン名)
    success_url = reverse_lazy('licenseapp:create_done')


class LicenseUpdateView(UpdateView):
    #利用するモデルを指定
    model = License
    #利用するフォームクラス名を指定
    form_class = LicenseForm
    #登録処理が正常終了した場合の遷移先を指定(空間名:パターン名)
    success_url = reverse_lazy('licenseapp:update_done')

def create_done(request):
    #登録処理が正常終了した場合に呼ばれるテンプレートを指定
    return render(request, 'licenseapp/create_done.html')


def update_done(request):
    #更新処理が正常終了した場合に呼ばれるテンプレートを指定
    return render(request, 'licenseapp/update_done.html')


class LicenseDeleteView(DeleteView):
    #利用するモデルを指定
    model = License
    #削除処理が正常終了した場合の遷移先を指定(空間名:パターン名)
    success_url = reverse_lazy('licenseapp:delete_done')


def delete_done(request):
    return render(request, 'licenseapp/delete_done.html')

