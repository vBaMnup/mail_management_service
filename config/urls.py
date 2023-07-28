from django.contrib import admin
from django.urls import path

from src.mailing import views
from config.yasg import swaggerurlpatterns


urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += swaggerurlpatterns
