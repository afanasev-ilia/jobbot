from django.urls import path

from report.apps import ReportConfig
from report.views import report_list

app_name = ReportConfig.name

urlpatterns = [
   path('v1/reports/', report_list),
]
