from django.contrib import admin

from src.mailing.models import Client, Mailing


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_filter = ("filter",)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "tag", "operator_code")
    search_fields = ("phone_number",)
    list_filter = ("tag", "operator_code")
