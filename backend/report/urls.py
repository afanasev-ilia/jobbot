
from django.urls import path

from report.apps import ReportConfig
from report.views import index, download_report

app_name = ReportConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('download_report', download_report, name='download_report')
]
