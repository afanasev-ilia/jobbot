from django.contrib import admin
from django.urls import include, path

from report.apps import ReportConfig

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('report.urls', namespace=ReportConfig.name)),
]
