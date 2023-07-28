from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


class Mailing(models.Model):
    """Mailing model"""

    mailing_id = models.AutoField(primary_key=True)
    start_datetime = models.DateTimeField("Date and time of mailing start")
    end_datetime = models.DateTimeField("Date and time of mailing end")
    filter = models.CharField("Filter", max_length=100)

    @property
    def to_sent(self):
        return self.start_datetime < timezone.now() < self.end_datetime

    def clean(self):
        if self.start_datetime > self.end_datetime < timezone.now():
            raise ValueError("Start time must be before end time")

    def __str__(self):
        return self.filter

    class Meta:
        verbose_name = "Mailing"
        verbose_name_plural = "Mailings"


class Client(models.Model):
    """Client model"""

    client_id = models.AutoField(primary_key=True)
    phone_number = models.CharField(
        max_length=11,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^7\d{10}$",
                message="Phone number must start with 7 and have a length of 11 digits.",
            )
        ],
    )
    operator_code = models.CharField(max_length=3)
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
