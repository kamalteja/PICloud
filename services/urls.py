from django.conf.urls import url
from django.contrib import admin

# from services import views

# urlpatterns = [
#     url(r'^$', views.services_list),
#     url(r'^create/', views.services_create),
#     url(r'^detail/', views.services_detail),
#     url(r'^update/', views.services_update),
#     url(r'^delete/', views.services_delete),

# ]

#------------OR----------

#from .views import (
#or
from services.views import (
	services_list,
	services_list_child,
	services_delete,
	services_update,
	services_detail,
	services_create)
 
urlpatterns = [
    url(r'^$', services_list),
    #url(r'^$', services_list_child),
    url(r'^create/', services_create),
    url(r'^id=(?P<id>\d+)/$', services_detail, name='detail'),
    url(r'^update/', services_update),
    url(r'^delete/', services_delete),

]