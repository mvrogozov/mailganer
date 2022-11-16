from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from celery import shared_task


@shared_task()
def send_email(
    subject,
    template,
    data,
    from_email,
    recipient_list
):
    # type: (str, str, dict, str, list) -> None
    '''Sending email'''

    html_body = render_to_string(template, data)
    send_mail(
        subject=subject,
        message=html_body,
        html_message=html_body,
        from_email=from_email,
        recipient_list=recipient_list
    )
