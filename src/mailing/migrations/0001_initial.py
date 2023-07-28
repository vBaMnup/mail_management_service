# Generated by Django 4.2.3 on 2023-07-28 17:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                ("client_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "phone_number",
                    models.CharField(
                        max_length=11,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must start with 7 and have a length of 11 digits.",
                                regex="^7\\d{10}$",
                            )
                        ],
                        verbose_name="Phone number",
                    ),
                ),
                (
                    "operator_code",
                    models.CharField(
                        editable=False, max_length=3, verbose_name="Operator code"
                    ),
                ),
                ("tag", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "Client",
                "verbose_name_plural": "Clients",
            },
        ),
        migrations.CreateModel(
            name="Mailing",
            fields=[
                ("mailing_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "start_datetime",
                    models.DateTimeField(verbose_name="Date and time of mailing start"),
                ),
                (
                    "end_datetime",
                    models.DateTimeField(verbose_name="Date and time of mailing end"),
                ),
                (
                    "operator_code_filter",
                    models.CharField(
                        blank=True,
                        max_length=3,
                        null=True,
                        verbose_name="Operator code",
                    ),
                ),
                (
                    "tag_filter",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Tag"
                    ),
                ),
            ],
            options={
                "verbose_name": "Mailing",
                "verbose_name_plural": "Mailings",
            },
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                ("message_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "datetime",
                    models.DateTimeField(
                        verbose_name="Date and time of message creation"
                    ),
                ),
                ("text", models.TextField(verbose_name="Message text")),
                (
                    "mailing_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="messages",
                        to="mailing.mailing",
                        verbose_name="Mailing",
                    ),
                ),
            ],
            options={
                "verbose_name": "Message",
                "verbose_name_plural": "Messages",
            },
        ),
    ]