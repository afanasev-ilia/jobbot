
from django.urls import path

from report.apps import ReportConfig
from report.views import index

app_name = ReportConfig.name

urlpatterns = [
   path('', index, name='index'),
]
