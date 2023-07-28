from django.contrib import admin
from django.urls import path, include

from config.yasg import swaggerurlpatterns

urlpatterns = [
    path("api/v1/", include("src.api.urls")),
    path("admin/", admin.site.urls),
]

urlpatterns += swaggerurlpatterns
