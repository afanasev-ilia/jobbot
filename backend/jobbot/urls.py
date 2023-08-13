from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


from report.apps import ReportConfig
from api.apps import ApiConfig

urlpatterns = [
    path('', include('report.urls', namespace=ReportConfig.name)),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace=ApiConfig.name)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
