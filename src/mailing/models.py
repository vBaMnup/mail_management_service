from django.db import models
from django.core.validators import RegexValidator


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
