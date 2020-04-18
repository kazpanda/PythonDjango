from django.urls import path
from django.urls import path
from . import views

# 空間名
app_name = 'licenseapp'

# パターン名
urlpatterns = [
    path('list/', views.LicenseListView.as_view(), name='license_list'),
    path('create/', views.LicenseCreateView.as_view(), name='license_create'),
    path('create_done/', views.create_done, name='create_done'),
    path('update/<int:pk>/', views.LicenseUpdateView.as_view(), name='license_update'),
    path('update_done/', views.update_done, name='update_done'),
    path('delete/<int:pk>/', views.LicenseDeleteView.as_view(), name='license_delete'),
    path('delete_done/', views.delete_done, name='delete_done'),

    ]