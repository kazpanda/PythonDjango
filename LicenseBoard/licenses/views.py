import pdb
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import UpdateView, ListView
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.urls import reverse

from .forms import NewPublicationForm, PostForm, NewOperationForm
from .models import T_License, T_Publication, Post, T_Operation


# --------------------------------------------
# ライセンス一覧表示
# --------------------------------------------
class LicenseListView(ListView):
    model = T_License
    context_object_name = 'licenses'
    template_name = 'home.html'


# --------------------------------------------
# 使用履歴一覧表示
# --------------------------------------------
class OperationListView(ListView):
    model = T_Operation
    context_object_name = 'operation'
    template_name = 'operation_list.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        # テンプレートでboard変数を使えるようにするkwargs['board']
        kwargs['html_obj'] = self.license
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.license = get_object_or_404(T_License, pk=self.kwargs.get('pk'))
        queryset = self.license.operations.order_by('-updated_at')
        return queryset


# --------------------------------------------
# 使用履歴新規発行
# --------------------------------------------
@login_required
def operation_new(request, pk):
    # DBから1つだけ取得 _object_ リストを取得するときは_list_
    db_obj = get_object_or_404(T_License, pk=pk)
    if request.method == 'POST':
        form = NewOperationForm(request.POST)
        # バリデーションチェック
        if form.is_valid():
            # formを保存する commit=False と指定することで、Modelインスタンスを取得
            topic = form.save(commit=False)
            # 外部Keyの登録
            topic.license = db_obj
            # 現在のuserを登録
            topic.starter = request.user
            # DB保存
            topic.save()
            Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user
            )
            return redirect('licenses:operation_posts', pk=pk, operation_pk=topic.pk)
    else:
        form = NewOperationForm()
    # render()関数は 、 第1引数としてrequestオブジェクトを 、
    # 第2引数としてテンプレート名を第3引数（任意）として辞書を受け取ります htmlオブジェクト名:オブジェクト
    # この関数はテンプレートを指定のコンテキストでレンダリングしそのHttpResponseオブジェクトを返します 。
    return render(request, 'operation_new.html', {'html_obj': db_obj, 'form': form})


# --------------------------------------------
# operationReply一覧表示
# --------------------------------------------
@login_required
def reply_operation(request, pk, operation_pk):
    topic = get_object_or_404(T_Operation, license__pk=pk, pk=operation_pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()

            topic.last_updated = timezone.now()
            topic.save()

            operation_url = reverse('licenses:operation_posts', kwargs={
                'pk': pk, 'operation_pk': operation_pk})

            operation_post_url = '{url}?page={page}#{id}'.format(
                url=operation_url,
                id=post.pk,
                page=topic.get_page_count()
            )

            return redirect(operation_post_url)
    else:
        form = PostForm()
    return render(request, 'reply_operation.html', {'topic': topic, 'form': form})


# --------------------------------------------
# ライセンス発行一覧表示
# --------------------------------------------
class PublicationListView(ListView):
    model = T_Publication
    context_object_name = 'publication'
    template_name = 'publication_list.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        # テンプレートでboard変数を使えるようにするkwargs['board']
        kwargs['html_obj'] = self.license
        # import pdb
        # pdb.set_trace()
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.license = get_object_or_404(T_License, pk=self.kwargs.get('pk'))
        queryset = self.license.publications.order_by(
            '-last_updated').annotate(replies=Count('posts') - 1)
        # import pdb
        # pdb.set_trace()
        return queryset


# --------------------------------------------
# Post一覧表示
# --------------------------------------------
class OperationPostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'operation_posts.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        session_key = 'viewed_topic_{}'.format(self.topic.pk)
        if not self.request.session.get(session_key, False):
            self.topic.views += 1
            self.topic.save()
            self.request.session[session_key] = True
        kwargs['topic'] = self.topic
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        # __pk は暗黙で __id__exact を表す
        self.topic = get_object_or_404(T_Operation, license__pk=self.kwargs.get(
            'pk'), pk=self.kwargs.get('operation_pk'))
        queryset = self.topic.posts.order_by('created_at')
        return queryset


# --------------------------------------------
# PublicationPost一覧表示
# --------------------------------------------
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'publication_posts.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        session_key = 'viewed_topic_{}'.format(self.topic.pk)
        if not self.request.session.get(session_key, False):
            self.topic.views += 1
            self.topic.save()
            self.request.session[session_key] = True
        kwargs['topic'] = self.topic
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        # __pk は暗黙で __id__exact を表す
        self.topic = get_object_or_404(T_Publication, license__pk=self.kwargs.get(
            'pk'), pk=self.kwargs.get('publication_pk'))
        queryset = self.topic.posts.order_by('created_at')
        return queryset


# --------------------------------------------
# ライセンス新規発行
# --------------------------------------------
@login_required
def publication_new(request, pk):
    # DBから1つだけ取得 _object_ リストを取得するときは_list_
    db_obj = get_object_or_404(T_License, pk=pk)
    if request.method == 'POST':
        form = NewPublicationForm(request.POST)
        # バリデーションチェック
        if form.is_valid():
            # formを保存する commit=False と指定することで、Modelインスタンスを取得
            topic = form.save(commit=False)
            # 外部Keyの登録
            topic.license = db_obj
            # 現在のuserを登録
            topic.starter = request.user
            # DB保存
            topic.save()
            Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user
            )
            return redirect('licenses:publication_posts', pk=pk, publication_pk=topic.pk)
    else:
        form = NewPublicationForm()
    # render()関数は 、 第1引数としてrequestオブジェクトを 、
    # 第2引数としてテンプレート名を第3引数（任意）として辞書を受け取ります htmlオブジェクト名:オブジェクト
    # この関数はテンプレートを指定のコンテキストでレンダリングしそのHttpResponseオブジェクトを返します 。
    return render(request, 'publication_new.html', {'html_obj': db_obj, 'form': form})


# --------------------------------------------
# Reply一覧表示
# --------------------------------------------
@login_required
def reply_publication(request, pk, publication_pk):
    topic = get_object_or_404(T_Publication, license__pk=pk, pk=publication_pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()

            topic.last_updated = timezone.now()
            topic.save()

            publication_url = reverse('licenses:publication_posts', kwargs={
                'pk': pk, 'publication_pk': publication_pk})

            publication_post_url = '{url}?page={page}#{id}'.format(
                url=publication_url,
                id=post.pk,
                page=topic.get_page_count()
            )

            return redirect(publication_post_url)
    else:
        form = PostForm()
    return render(request, 'reply_publication.html', {'topic': topic, 'form': form})


# --------------------------------------------
# Post更新画面
# --------------------------------------------
@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    fields = ('message', )
    template_name = 'edit_post.html'
    pk_url_kwarg = 'post_pk'
    context_object_name = 'post'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)

    def form_valid(self, form):
        post = form.save(commit=False)
        post.updated_by = self.request.user
        post.updated_at = timezone.now()
        post.save()
        return redirect('licenses:publication_posts',
                        pk=post.topic.license.pk, publication_pk=post.topic.pk)
