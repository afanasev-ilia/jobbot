from django.contrib import admin

from report.models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = (
        'employee',
        'order',
        'item_order',
        'execution_time',
        'image',
        'report_date',
    )
    empty_value_display = '-пусто-'
    list_editable = (
        'order',
        'item_order',
        'execution_time',
    )
    search_fields = (
        'employee',
        'order',
    )
    list_filter = (
        'employee',
        'order',
    )
