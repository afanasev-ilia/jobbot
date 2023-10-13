from django.urls import path

from api.apps import ApiConfig
from api.views import clean_report_list, work_report_list


app_name = ApiConfig.name

urlpatterns = [
    path('v1/clean_reports/', clean_report_list),
    path('v1/work_reports/', work_report_list),
]
