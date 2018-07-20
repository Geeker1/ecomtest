from celery import task 
from celery.utils.log import get_task_logger
from .emails import send_feedback_email

from django.core import mail

logger = get_task_logger(__name__)

@task
def send_feedback_email_task(email):
    """sends an email when feedback form is filled successfully"""
    logger.info("SENT THE EMAIL")
    return send_feedback_email(email)