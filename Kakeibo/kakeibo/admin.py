from django.contrib import admin
from .models import Category, Kakeibo, License

#追加
class KakeiboAdmin(admin.ModelAdmin):
    list_display=('date','category','license','money','memo')

admin.site.register(Category)
admin.site.register(License)
admin.site.register(Kakeibo,KakeiboAdmin)
