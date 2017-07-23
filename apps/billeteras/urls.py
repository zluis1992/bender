from django.conf.urls import url, include
from apps.billeteras.views import index

urlpatterns = [
    url(r'^$', index),
]