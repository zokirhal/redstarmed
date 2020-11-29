from django.urls import path
from .views import *


urlpatterns = [
    path('', Bosh_Sahifa.as_view(), name='bosh_sahifa'),
    path('about/', Biz_Haqimizda.as_view(), name='biz_haqimizda'),
    path('gallerey/', Galereya.as_view(), name='galereya'),
    path('service', Xizmatlarimiz.as_view(), name='service'),
    path('contacts', Aloqa.as_view(), name='aloqa'),
]