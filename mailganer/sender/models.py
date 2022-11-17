# -*- coding: utf-8 -*-
from django.db import models


class Buyers(models.Model):
    name = models.CharField(
        'Имя',
        max_length=100
    )
    surname = models.CharField(
        'Фамилия',
        max_length=100
    )
    email = models.EmailField(
        'email',
        max_length=254
    )
    birth_date = models.DateTimeField(
        'Дата рождения',
    )

    def __str__(self):
        return '{} {}'.format(self.surname, self.name)


class CheckedEmail(models.Model):
    template_name = models.CharField(
        'Шаблон',
        max_length=254
    )
    check_date = models.DateTimeField(
        'Дата открытия',
        auto_now_add=True
    )
    buyer = models.ForeignKey(
        Buyers,
        null=False,
        related_name='checked',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{} - {}'.format(self.buyer, self.template_name)
