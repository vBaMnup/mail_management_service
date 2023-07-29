from rest_framework import viewsets

from src.mailing.models import Mailing, Message, Client
from src.mailing.serializers import (
    MailingSerializer,
    MessageSerializer,
    ClientSerializer,
)
from src.mailing.tasks import send_mailing


class MailingViewSet(viewsets.ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        message = serializer.save()
        mailing = message.mailing_id
        if mailing.start_datetime <= message.datetime <= mailing.end_datetime:
            send_mailing.apply_async(
                kwargs={"message_id": message.message_id},
                eta=message.datetime,
            )
        else:
            pass


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
