from django import views
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('membership/', membership, name='membership'),
]