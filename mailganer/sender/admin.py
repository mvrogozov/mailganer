# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Buyers, CheckedEmail


class BuyerAdmin(admin.ModelAdmin):
    list_display = (
        'surname',
        'name',
        'email',
        'birth_date'
    )


class CheckedEmailAdmin(admin.ModelAdmin):
    list_display = (
        'template_name',
        'check_date',
        'buyer'
    )


admin.site.register(Buyers, BuyerAdmin)
admin.site.register(CheckedEmail, CheckedEmailAdmin)
