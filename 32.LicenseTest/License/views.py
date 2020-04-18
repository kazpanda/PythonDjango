from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView, DetailView
from .models import *
from .forms import LicenseForm, ParentForm
from django.urls import reverse_lazy
from extra_views import InlineFormSetFactory, CreateWithInlinesView, UpdateWithInlinesView, SearchableListMixin, NamedFormsetsMixin, GenericInlineFormSetFactory


# ------------------------------------------------------------
# 使用履歴画面
# ------------------------------------------------------------
# 使用履歴インラインクラス
class OperationHistoryInline(InlineFormSetFactory):
    model = T_OperationHistory
    fields = [
        'author', 'license', 'starting_count', 'weekly_report_count',
        'monthly_report_count', 'memo'
    ]
    factory_kwargs = {
        'extra': 1,
        'max_num': None,
        'can_order': False,
        'can_delete': True
    }
    #formset_kwargs = {'auto_id': 'my_id_%s'}


# 使用履歴新規作成クラス
class OperationHistoryCreateView(CreateWithInlinesView):
    model = T_License
    fields = [
        'company', 'language', 'application', 'display_number', 'hid',
        'remaining_point', 'memo'
    ]
    context_object_name = 'parent'
    inlines = [OperationHistoryInline]
    template_name = 'License/operation_history_create.html'
    success_url = reverse_lazy('License:create_done')


# 使用履歴更新クラス
class OperationHistoryUpdateView(UpdateWithInlinesView):
    model = T_License
    form_class = ParentForm
    inlines = [OperationHistoryInline]
    template_name = 'License/operation_history_update.html'
    success_url = reverse_lazy('License:create_done')


# 使用履歴リスト表示クラス
class OperationHistoryView(DetailView):
    # uerysetを使う際は、単純に以下のようにしても大丈夫
    # 内部では、このquerysetに対して、pkを使って.filter(pk=pk)のようなことを行っています。
    # 利用するモデルを指定
    model = T_OperationHistory
    # デフォルト値は
    # <app name>/<model name>_detail.html
    template_name = 'License/operation_history_list.html'

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        #messages.success(self.request, '「{}」を削除しました'.format(self.object))
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_list = T_OperationHistory.objects.filter(
            license_id=self.kwargs['pk'])  # pkを指定してデータを絞り込む
        context['object_list'] = data_list
        return context

'''
class TagInline(GenericInlineFormSetFactory):
    model = Tag
    fields = '__all__'


# If you want more control over the names of your formsets (as opposed to iterating over inlines), you can use NamedFormsetsMixin.
class CreateOrderView(NamedFormsetsMixin, CreateWithInlinesView):
    model = Order
    inlines = [OperationHistoryInline, TagInline]
    inlines_names = ['Items', 'Tags']
    fields = '__all__'

# Are you just trying to set the initial value of the extra field?
class MyChildForm(forms.ModelForm):
    my_extra = forms.CharField(label='Extra', max_length=20)

    def __init__(self, *args, **kwargs):
        super(MyChildForm, self).__init__(*args, **kwargs)
        if self.instance:
            extra_value = MyExtraModel.objects.get(child=self.instance)
            self.fields['my_extra'].initial = extra_value.favorite_toy


https://code-examples.net/ja/q/bfdd28


FatherInlineFormSet = inlineformset_factory(Father,
                                            Son,
                                            form=SonInline,
                                            extra=1,
                                            can_delete=False,
                                            can_order=False)


class CreateFatherView(CreateView):
    template_name = 'father_create.html'
    model = Father
    form_class = FatherForm  # the parent object's form

    # On successful form submission
    def get_success_url(self):
        return reverse('father-created')

    # Validate forms
    def form_valid(self, form):
        ctx = self.get_context_data()
        inlines = ctx['inlines']
        if inlines.is_valid() and form.is_valid():
            self.object = form.save()  # saves Father and Children
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    # We populate the context with the forms. Here I'm sending
    # the inline forms in `inlines`
    def get_context_data(self, **kwargs):
        ctx = super(CreateFatherView, self).get_context_data(**kwargs)
        if self.request.POST:
            ctx['form'] = FatherForm(self.request.POST)
            ctx['inlines'] = FatherInlineFormSet(self.request.POST)
        else:
            ctx['form'] = Father()
            ctx['inlines'] = FatherInlineFormSet()
        return ctx
'''

# ------------------------------------------------------------
# ライセンス発行履歴画面
# ------------------------------------------------------------
# ライセンス履歴クラス
# IMPORTANT: Note that when using InlineFormSetFactory,
# model should be the inline model and not the parent model.
class LicenseHistoryInline(InlineFormSetFactory):
    model = T_LicenseHistory
    fields = [
        'author', 'license', 'request_category', 'begin_date', 'end_date',
        'mac_address', 'price', 'grant_point', 'remaining_point',
        'renewal_deadline_notification', 'renewal_application_accepted',
        'renewal_application_send', 'renewal_key_publish_notification',
        'discontinued_product_collection', 'memo'
    ]
    factory_kwargs = {
        'extra': 1,
        'max_num': None,
        'can_order': False,
        'can_delete': True
    }
    #formset_kwargs = {'auto_id': 'my_id_%s'}


# ライセンス履歴新規作成クラス
class LicenseHistoryCreateView(CreateWithInlinesView):
    model = T_License
    fields = [
        'company', 'language', 'application', 'display_number', 'hid',
        'remaining_point', 'memo'
    ]
    context_object_name = 'parent'
    inlines = [LicenseHistoryInline]
    template_name = 'License/license_history_create.html'
    success_url = reverse_lazy('License:create_done')


# ライセンス履歴更新クラス
class LicenseHistoryUpdateView(UpdateWithInlinesView):
    model = T_License
    form_class = ParentForm
    inlines = [LicenseHistoryInline]
    template_name = 'License/license_history_create.html'
    success_url = reverse_lazy('License:create_done')


# ライセンス履歴リスト表示クラス
class LicenseHistoryView(DetailView):
    # uerysetを使う際は、単純に以下のようにしても大丈夫
    # 内部では、このquerysetに対して、pkを使って.filter(pk=pk)のようなことを行っています。
    # 利用するモデルを指定
    model = T_LicenseHistory
    # デフォルト値は
    # <app name>/<model name>_detail.html
    template_name = 'License/license_history_list.html'

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        #messages.success(self.request, '「{}」を削除しました'.format(self.object))
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_list = T_LicenseHistory.objects.filter(
            license_id=self.kwargs['pk'])  # pkを指定してデータを絞り込む
        context['object_list'] = data_list
        return context


# ------------------------------------------------------------
# メイン画面
# ------------------------------------------------------------
# 一覧表示
class LicenseListView(ListView):
    # model = Licenseとすることで、License.objects.all()を裏側で行う
    # queryset = License.objects.all()
    # 利用するモデルを指定
    model = T_License
    # データを渡すテンプレートファイルを指定
    template_name = 'License/license_list.html'

    # デフォルト値は
    # <app name>/<model name>_list.html
    # テーブルの全データを取得するメソッドを定義
    def queryset(self):
        return T_License.objects.all()


# 新規作成画面
class LicenseCreateView(CreateView):

    # 利用するモデルを指定
    model = T_LicenseHistory
    # 利用するフォームクラス名を指定
    form_class = LicenseForm
    # 登録処理が正常終了した場合の遷移先を指定
    success_url = reverse_lazy('License:create_done')


# 更新画面
class LicenseUpdateView(UpdateView):
    # 利用するモデルを指定
    model = T_License
    # 利用するフォームクラス名を指定
    form_class = LicenseForm
    # 登録処理が正常終了した場合の遷移先を指定
    success_url = reverse_lazy('License:update_done')


# 作成完了画面
def create_done(request):
    # 登録処理が正常終了した場合に呼ばれるテンプレートを指定
    return render(request, 'License/create_done.html')


# 更新完了
def update_done(request):
    # 更新処理が正常終了した場合に呼ばれるテンプレートを指定
    return render(request, 'License/update_done.html')


# 削除画面
class LicenseDeleteView(DeleteView):
    # 利用するモデルを指定
    model = T_License
    # 削除処理が正常終了した場合の遷移先を指定
    success_url = reverse_lazy('License:delete_done')


# 削除完了画面
def delete_done(request):
    return render(request, 'License/delete_done.html')


class SuccessView(TemplateView):
    template_name = "License/success.html"
