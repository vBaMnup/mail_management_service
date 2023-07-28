from rest_framework import serializers
from django.utils import timezone

from src.mailing.models import Mailing, Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class MailingSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Mailing
        fields = "__all__"

    def validate(self, attrs):
        start_datetime = attrs.get("start_datetime")
        end_datetime = attrs.get("end_datetime")

        if start_datetime and end_datetime:
            if end_datetime <= start_datetime:
                raise serializers.ValidationError(
                    "End mailing date must be greater than start date."
                )

            current_time = timezone.now()
            if end_datetime <= current_time:
                raise serializers.ValidationError(
                    "End mailing date must be greater than current time."
                )

        return attrs
