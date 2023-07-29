from django.contrib import admin

from src.mailing.models import Client, Mailing, Message


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    pass


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "tag", "operator_code")
    search_fields = ("phone_number",)
    list_filter = ("tag", "operator_code")


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    search_fields = ("text",)
    list_filter = ("datetime",)
