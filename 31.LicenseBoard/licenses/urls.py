from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views


app_name = 'licenses'


urlpatterns = [
    # Home画面
    path('', views.LicenseListView.as_view(), name='home'),

    # --------------------------------------------
    # Operation
    # --------------------------------------------
    # Operation一覧表示
    path('operation/<int:pk>/',
         views.OperationListView.as_view(),
         name='operation_list'),

    # Operation新規作成
    path('operation/<int:pk>/new/',
         views.operation_new, name='operation_new'),

    # OperationPost一覧
    path('operation/<int:pk>/operations/<int:operation_pk>/',
         views.OperationPostListView.as_view(), name='operation_posts'),

    # OperationReply一覧
    path('operation/<int:pk>/operations/<int:operation_pk>/reply/',
         views.reply_operation, name='reply_operation'),

    # OperationReply編集
    path('operation/<int:pk>/operations/<int:operation_pk>/posts/<int:post_pk>/edit/',
         views.PostUpdateView.as_view(), name='edit_post'),


    # --------------------------------------------
    # Publication
    # --------------------------------------------
    # Publication一覧表示
    path('publication/<int:pk>/',
         views.PublicationListView.as_view(),
         name='publication_list'),

    # Publication新規作成
    path('publication/<int:pk>/new/',
         views.publication_new, name='publication_new'),


    # PublicationPost一覧
    path('publication/<int:pk>/publications/<int:publication_pk>/',
         views.PostListView.as_view(), name='publication_posts'),

    # PublicationReply一覧
    path('publication/<int:pk>/publications/<int:publication_pk>/reply/',
         views.reply_publication, name='reply_publication'),

    # PublicationReply編集
    path('publication/<int:pk>/publications/<int:publication_pk>/posts/<int:post_pk>/edit/',
         views.PostUpdateView.as_view(), name='edit_post'),


    # --------------------------------------------
    # sign
    # --------------------------------------------
    # Sign up
    path('signup/', accounts_views.signup, name='signup'),

    # log in
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # log out
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


    # --------------------------------------------
    #　Password
    # --------------------------------------------
    path('reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password_reset.html',
             email_template_name='password_reset_email.html',
             subject_template_name='password_reset_subject.txt'
         ),
         name='password_reset'),

    path('reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'),
         name='password_reset_complete'),

    path('settings/account/',
         accounts_views.UserUpdateView.as_view(), name='my_account'),

    path('settings/password/',
         auth_views.PasswordChangeView.as_view(
             template_name='password_change.html'),
         name='password_change'),

    path('settings/password/done/',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='password_change_done.html'),
         name='password_change_done'),


]
