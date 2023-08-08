from django.urls import path

from report.apps import ReportConfig
from report.views import report_list
from report.views import export_excel

app_name = ReportConfig.name

urlpatterns = [
   path('v1/reports/', report_list),
   path('export/', export_excel, name='export_excel'),
]
