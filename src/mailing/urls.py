from django.urls import path, include
from rest_framework import routers

from src.mailing.views import MailingViewSet, MessageViewSet, ClientViewSet

router = routers.DefaultRouter()
router.register("mailings", MailingViewSet)
router.register("messages", MessageViewSet)
router.register("clients", ClientViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
