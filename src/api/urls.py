from django.urls import path, include


urlpatterns = [
    path("", include("src.mailing.urls")),
]
