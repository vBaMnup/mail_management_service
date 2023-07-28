from rest_framework import viewsets

from src.mailing.models import Mailing, Message, Client
from src.mailing.serializers import MailingSerializer, MessageSerializer, ClientSerializer


class MailingViewSet(viewsets.ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
