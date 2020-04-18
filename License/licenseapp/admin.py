from django.contrib import admin
from .models import Category, Company, Language, License, LicenseDetail, Software

# 追加


class LicenseAdmin(admin.ModelAdmin):
    list_display = ('date', 'category', 'license_detail',
                    'company', 'language', 'money', 'comment')


admin.site.register(Category)
admin.site.register(Software)
admin.site.register(Company)
admin.site.register(Language)
admin.site.register(LicenseDetail)

admin.site.register(License, LicenseAdmin)
