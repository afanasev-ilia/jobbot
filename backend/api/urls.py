from django.urls import path

from api.apps import ApiConfig
from api.views import report_list


app_name = ApiConfig.name

urlpatterns = [
   path('v1/reports/', report_list),
]
