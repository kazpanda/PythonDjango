from django.contrib import admin
from .models import *


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('license', 'begin_date',
                    'end_date', 'mac_address', 'price', 'grant_points',
                    'remaining_point', 'renewal_deadline_notification',
                    'renewal_application_accepted', 'renewal_application_send',
                    'renewal_key_publish_notification',
                    'discontinued_product_collection', 'memo')


class LicenseAdmin(admin.ModelAdmin):
    list_display = ('company', 'language', 'application',
                    'display_name', 'hid','memo')


class OperationAdmin(admin.ModelAdmin):
    list_display = ('starting_count', 'weekly_report_count', 'monthly_report_count',
                    'memo')


admin.site.register(M_Language)
admin.site.register(M_Company)
admin.site.register(M_Application)
admin.site.register(M_Message)
admin.site.register(M_RequestCategory)

admin.site.register(T_Operation, OperationAdmin)
admin.site.register(T_Publication, PublicationAdmin)
admin.site.register(T_License, LicenseAdmin)


#admin.site.register(T_License)
#admin.site.register(T_Publication)
