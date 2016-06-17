from django.conf.urls import url
from django.contrib import admin

from auth.views import (
	auth_login)

urlpatterns = [
	url(r'^$', auth_login),
]