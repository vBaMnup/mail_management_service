from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone


class Mailing(models.Model):
    """Mailing model"""

    mailing_id = models.AutoField(primary_key=True)
    start_datetime = models.DateTimeField("Date and time of mailing start")
    end_datetime = models.DateTimeField("Date and time of mailing end")
    operator_code_filter = models.CharField(
        "Operator code", max_length=3, blank=True, null=True
    )
    tag_filter = models.CharField("Tag", max_length=100, blank=True, null=True)

    def get_clients(self):
        clients = Client.objects.all()
        if self.operator_code_filter:
            clients = clients.filter(operator_code=self.operator_code_filter)
        if self.tag_filter:
            clients = clients.filter(tag=self.tag_filter)
        return clients

    @property
    def to_sent(self):
        return self.start_datetime < timezone.now() < self.end_datetime

    def clean(self):
        if self.start_datetime >= self.end_datetime:
            raise ValueError("Start time must be before end time")

    def __str__(self):
        return f"start: {self.start_datetime}, end: {self.end_datetime}"

    class Meta:
        verbose_name = "Mailing"
        verbose_name_plural = "Mailings"


class Client(models.Model):
    """Client model"""

    client_id = models.AutoField(primary_key=True)
    phone_number = models.CharField(
        "Phone number",
        max_length=11,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^7\d{10}$",
                message="Phone number must start with 7 and have a length of 11 digits.",
            )
        ],
    )
    operator_code = models.CharField("Operator code", max_length=3, editable=False)
    tag = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.operator_code = self.phone_number[1:4]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"


class Message(models.Model):
    """Message model"""

    message_id = models.AutoField(primary_key=True)
    datetime = models.DateTimeField("Date and time of message creation")
    mailing_id = models.ForeignKey(
        Mailing,
        on_delete=models.CASCADE,
        related_name="messages",
        verbose_name="Mailing",
    )
    text = models.TextField("Message text")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
