# -*- coding: utf-8 -*-
import os
import logging
from django.views.generic import TemplateView, View
from django.conf import settings 
from django.http import HttpResponse, request
from .utils import send_email
from .models import Buyers
from logging.handlers import RotatingFileHandler


LOG_FILE_NAME = 'email_sender.log'
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


class SenderView(View):
    template_name = 'sender/index.html'
    data = {'name': 'Petya', 'age': 37}
    def get(self, request, *args, **kwargs):
        buyers = Buyers.objects.all()
        print(Buyers.objects.count())

        for buyer in buyers:
            data={
                'name': u'%s' % buyer.name,
                'surname': buyer.surname,
                'birthday': buyer.birth_date,
                'domain': settings.PROJECT_DOMAIN,
                'email': buyer.email,
                'id': buyer.id
            }
            print('data= ', data)
            print(buyer.email)
            print(settings.PROJECT_DOMAIN)
            send_email.delay(
                subject='Тема письма',
                template='email_template_2.html',
                data=data,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[buyer.email]
            )
        return HttpResponse('done')
        

class PixelView(View):
    template_name = 'sender/index.html'
    def get(self, request, *args, **kwargs):
        try:
            image_data = open(os.path.join(settings.MEDIA_ROOT, 'pixel.png'), 'rb').read()
        except Exception:
            print('Error opening pixel file')
            return None
        user_id = kwargs.get('user')
        logger.info('User '+user_id+' opened email')
        return HttpResponse(image_data, content_type="image/png")
