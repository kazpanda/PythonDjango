from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('licenseapp.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url('license/', include(debug_toolbar.urls)),
    ]