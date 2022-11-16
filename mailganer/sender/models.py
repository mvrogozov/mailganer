
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class Buyers(models.Model):
    name=models.CharField(
        'Name',
        max_length=100
    )
    surname=models.CharField(
        'Surname',
        max_length=100
    )
    email=models.EmailField(
        'email',
        max_length=254
    )
    birth_date=models.DateField(
        'Birthday',
    )

    def __unicode__(self):
        return u'%s'%(self.surname)

    def __str__(self):
        return self.email
