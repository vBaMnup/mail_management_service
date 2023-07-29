from celery import shared_task
from celery.utils.log import get_task_logger

from src.mailing.models import Mailing, Message

logger = get_task_logger(__name__)


@shared_task
def send_mailing(message_id):
    try:
        message = Message.objects.get(message_id=message_id)
        mailing = message.mailing_id
        if mailing.start_datetime <= message.datetime <= mailing.end_datetime:
            clients = mailing.get_clients()
            message = message.text
            print(f'Message "{message}" sent to {len(clients)} {clients} clients')
    except Mailing.DoesNotExist:
        print(f"Mailing with id {mailing.mailing_id} does not exist")
