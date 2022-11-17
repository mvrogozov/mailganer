from django.conf.urls import url

from .views import PixelView, SenderApiView

app_name = 'sender'

urlpatterns = [
    url(r'^send/', SenderApiView.as_view(), name='sender_api'),
    url(
        r'^open-tracking/(?P<user>[0-9]+)/(?P<template_name>[A-Z0-9a-z._-]+)/$',
        PixelView.as_view(), name='pixel_view'
    ),
]
