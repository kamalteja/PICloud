from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import services #OR from services.models import services
# Create your views here.

def services_create(request):
	return HttpResponse("<h1>Create</h1>")

def services_detail(request, id):
	#return HttpResponse("<h1>Detail</h1>")
	#instance = services.objects.get(id=6)
	instance = get_object_or_404(services, id=id)
	list_data = {
		"header":	"Detailed Information",
		"Service_title": instance.service_name,
		"App": instance
	}
	return render(request, "detail.html", list_data)


def services_list(request):		#Listing the services

	# if request.user.is_authenticated():
	# 	list_data = {
	# 	"title": "List of Services",
	# 	"Apps": {"sshd", "apache2"},
	# 	}
	# else:
	# 	list_data = {
	# 	"title": "Authentication Required"
	# 	}
	service_list = services.objects.all()
	list_data = {
		"title": "List of Services",
		"Apps": service_list
	}
	return render(request, "list.html", list_data)

def services_update(request):
	return HttpResponse("<h1>Update</h1>")

def services_delete(request):
	return HttpResponse("<h1>Delete</h1>")