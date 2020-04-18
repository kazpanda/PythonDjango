from django.contrib import admin
from django.conf import settings
from django.urls import path, include


urlpatterns = [
    # Top画面
    path('', include('licenses.urls')),
    # 管理画面
    path('admin/', admin.site.urls),
]


# Debug設定
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
