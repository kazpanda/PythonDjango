from django.conf import settings
from django.urls import path, include
from . import views

app_name = 'License'

urlpatterns = [

    # ------------------------------------------------------------
    # メイン画面
    # ------------------------------------------------------------
    # リスト表示
    path('', views.LicenseListView.as_view(), name='list'),
    # 新規作成
    path('create/', views.LicenseCreateView.as_view(), name='create'),
    path('create_done/', views.create_done, name='create_done'),
    # 更新
    path('update/<int:pk>/', views.LicenseUpdateView.as_view(), name='update'),
    path('update_done/', views.update_done, name='update_done'),
    # 削除
    path('delete/<int:pk>/', views.LicenseDeleteView.as_view(), name='delete'),
    path('delete_done/', views.delete_done, name='delete_done'),

    # ------------------------------------------------------------
    # ライセンス履歴画面
    # ------------------------------------------------------------
    # ライセンス履歴表示
    path('license_history_list/<int:pk>/',
         views.LicenseHistoryView.as_view(),
         name='license_history_list'),

    # ライセンス履歴新規作成
    path('create_license_history/',
         views.LicenseHistoryCreateView.as_view(),
         name='create_license_history'),

    # ライセンス履歴更新
    path('update_license_history/<int:pk>/',
         views.LicenseHistoryUpdateView.as_view(),
         name='update_license_history'),

    # ------------------------------------------------------------
    # 使用履歴画面
    # ------------------------------------------------------------
    # 使用履歴表示
    path('operation_history_list/<int:pk>/',
         views.OperationHistoryView.as_view(),
         name='operation_history_list'),
    # 使用履歴新規作成
    path('operation_history_create/',
         views.OperationHistoryCreateView.as_view(),
         name='operation_history_create'),

    # 使用履歴更新
    path('operation_history_update/<int:pk>/',
         views.OperationHistoryUpdateView.as_view(),
         name='operation_history_update'),

    # 成功画面
    path('success/', views.SuccessView.as_view(), name='success'),
]
