from django.contrib import admin

from report.models import Employee, Report


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
    )
    list_filter = (
        'employee',
        'order',
    )

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'external_id',
        'full_name',
    )
    empty_value_display = '-пусто-'
    list_editable = (
        'full_name',
    )
    search_fields = (
        'full_name',
    )
    list_filter = (
        'full_name',
    )
