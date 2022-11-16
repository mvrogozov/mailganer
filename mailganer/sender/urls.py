from django.conf.urls import url
from .views import SenderView, PixelView

app_name = 'sender'

urlpatterns = [
    url(r'^index/', SenderView.as_view(), name='sender_index'),
    url(r'^open-tracking/(?P<user>[0-9]+)/$', PixelView.as_view(), name='pixel_view')
]
