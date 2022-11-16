# -*- coding: utf-8 -*-
import os
import logging
from django.conf import settings 
from .utils import send_email
from .models import Buyers
from logging.handlers import RotatingFileHandler
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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
            data={
                'name': buyer.name,
                'surname': buyer.surname,
                'birthday': buyer.birth_date,
                'domain': settings.PROJECT_DOMAIN,
                'email': buyer.email,
                'id': buyer.id
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
        return Response("OK", status=status.HTTP_200_OK)


class PixelView(APIView):
    """
    Email reading check.
    """
    def get(self, request, *args, **kwargs):
        try:
            image_data = open(os.path.join(settings.MEDIA_ROOT, 'pixel.png'), 'rb').read()
        except Exception:
            logger.error('Pixel picture error')
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        user_id = kwargs.get('user')
        logger.info('User '+user_id+' opened email')
        return Response(image_data, content_type='image/png')
