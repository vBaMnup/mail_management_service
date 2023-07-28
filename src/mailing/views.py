from rest_framework import viewsets

from src.mailing.models import Mailing, Message
from src.mailing.serializers import MailingSerializer, MessageSerializer


class MailingViewSet(viewsets.ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
