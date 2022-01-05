from django.contrib import admin
from django.urls import path, re_path
from .views import home, contact


urlpatterns = [
    re_path(r'^$',home , name='home'),
    re_path(r'^contato/$',contact , name='contact')
]