from django.conf.urls import url
from django.contrib import admin

from auth.views import (
	auth_login,
	auth_logout,
	auth_warn,
	relief,
	)

urlpatterns = [
	url(r'^$', auth_warn),
	url(r'authIn$', auth_login),
	url(r'authOut$', auth_logout),
	url(r'relief$', relief),
]