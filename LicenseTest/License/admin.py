from django.contrib import admin
from .models import *


class OperationHistoryAdmin(admin.ModelAdmin):
    list_display = ('author', 'license', 'starting_count',
                    'weekly_report_count', 'monthly_report_count', 'memo')


class LicenseHistoryAdmin(admin.ModelAdmin):
    list_display = ('author', 'license', 'request_category', 'begin_date',
                    'end_date', 'mac_address', 'price', 'grant_point',
                    'remaining_point', 'renewal_deadline_notification',
                    'renewal_application_accepted', 'renewal_application_send',
                    'renewal_key_publish_notification',
                    'discontinued_product_collection', 'memo')


class LicenseAdmin(admin.ModelAdmin):
    list_display = ('author', 'company', 'language', 'application',
                    'display_number', 'hid', 'remaining_point', 'memo')


admin.site.register(M_Language)
admin.site.register(M_Company)
admin.site.register(M_Application)
admin.site.register(M_Message)
admin.site.register(M_RequestCategory)

admin.site.register(T_OperationHistory, OperationHistoryAdmin)
admin.site.register(T_LicenseHistory, LicenseHistoryAdmin)
admin.site.register(T_License, LicenseAdmin)
