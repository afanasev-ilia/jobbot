from django.contrib import admin

from report.models import Employee, WorkReport, CleanReport


@admin.register(WorkReport)
class WorkReportAdmin(admin.ModelAdmin):
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
        'order',
    )
    list_filter = (
        'employee',
    )


@admin.register(CleanReport)
class CleanReportAdmin(admin.ModelAdmin):
    list_display = (
        'employee',
        'image',
        'report_date',
    )
    empty_value_display = '-пусто-'
    search_fields = (
        'employee',
    )
    list_filter = (
        'report_date',
    )


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'external_id',
        'full_name',
        'name',
    )
    empty_value_display = '-пусто-'
    list_editable = (
        'full_name',
        'name',
    )
    search_fields = (
        'full_name',
    )
    list_filter = (
        'full_name',
    )
