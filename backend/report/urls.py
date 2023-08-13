
from django.urls import path

from report.apps import ReportConfig
from report.views import export_excel

app_name = ReportConfig.name

urlpatterns = [
   path('', export_excel, name='export_excel'),
]
