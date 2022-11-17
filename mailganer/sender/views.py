# -*- coding: utf-8 -*-
import logging
import os
from logging.handlers import RotatingFileHandler

from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Buyers, CheckedEmail
from .tasks import send_email

LOG_FILE_NAME = 'email_sender.log'
SUBJECT = 'Тема письма'
EMAIL_TEMPLATE = 'email_template_2.html'
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = RotatingFileHandler(
    filename=LOG_FILE_NAME,
    maxBytes=5000000,
    backupCount=5
)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
handler.setFormatter(formatter)
logger.addHandler(handler)


class SenderApiView(APIView):
    """
    Send emails.
    """
    def get(self, request):
        buyers = Buyers.objects.all()
        timeout = int(request.data.get('timeout', 0))
        for buyer in buyers:
            data = {
                'name': buyer.name,
                'surname': buyer.surname,
                'birthday': buyer.birth_date,
                'domain': settings.PROJECT_DOMAIN,
                'email': buyer.email,
                'id': buyer.id,
                'template_name': EMAIL_TEMPLATE
            }
            send_email.apply_async(
                kwargs={
                    'subject': SUBJECT,
                    'template': EMAIL_TEMPLATE,
                    'data': data,
                    'from_email': settings.EMAIL_HOST_USER,
                    'recipient_list': [buyer.email]
                },
                countdown=timeout
            )
            timeout += timeout
        return Response("OK", status=status.HTTP_200_OK)


class PixelView(APIView):
    """
    Email reading check.
    """
    def get(self, request, *args, **kwargs):
        try:
            image_data = open(
                os.path.join(settings.MEDIA_ROOT, 'pixel.png'), 'rb'
            ).read()
        except Exception:
            logger.error('Pixel picture error')
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        user_id = int(kwargs.get('user'))
        template_name = kwargs.get('template_name')
        user = get_object_or_404(Buyers, id=user_id)
        CheckedEmail.objects.get_or_create(
            template_name=template_name,
            buyer=user
        )
        logger.info(
            'User {} opened {}'.format(user, template_name)
        )
        return Response(image_data, content_type='image/png')
