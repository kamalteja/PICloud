from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import services #OR from services.models import services
# Create your views here.
import re
import os
import subprocess
from django.utils import timezone

def services_create(request):
	return HttpResponse("<h1>Create</h1>")

def services_detail(request, id):
	if request.user.is_authenticated():
		list_data = services_detail_child(request, id)
	else:
		list_data = {
		"header": ""
		}
	return render(request, "detail.html", list_data)

def services_list(request):
	if request.user.is_authenticated():
		list_data = services_list_child()
	else:
		list_data = {
		"title": ""
		}
	return render(request, "list.html", list_data)
	
def services_update(request, id):
	serName = request.POST.get('serName')
	if 'switch' in request.POST.keys():
		switch = request.POST.get('switch')
		print "%s: %s, id: %s" %(serName, switch, id)
		py_shell = subprocess.Popen(["pgrep",serName], stdout=subprocess.PIPE)
	 	service_pid = re.sub(r'(\d)\n(\d)', r'\1,\2',py_shell.communicate()[0])
	 	service_pid = re.sub(r'\n', '', service_pid)
		ser = services(id=id, service_name=serName, current_status="UP", prev_status="DOWN", last_updated_time=timezone.now(), pid=service_pid)
	 	ser.save()
	elif 'switch' not in request.POST.keys():
		switch = "OFF"
		print "%s: %s, id: %s" %(serName, switch, id)
		get_service = services.objects.filter(service_name=serName)
		for obj in get_service:
			service_pid = re.sub(r',', ' ', obj.pid)
			py_shell = subprocess.Popen(["kill",service_pid,"2>&1"], stdout=subprocess.PIPE)
			ser = services(id=id, service_name=serName, current_status="DOWN", prev_status="UP", last_updated_time=timezone.now(), pid="Process Output: "+py_shell)
			ser.save()

def services_delete(request):
	return HttpResponse("<h1>Delete</h1>")

def services_list_child():
	py_shell = subprocess.Popen(["service","--status-all"], stdout=subprocess.PIPE)
	service_data = py_shell.communicate()[0]
	contentToArray=re.findall(r'\s*\[\s+(\+|\-)\s+\]\s+(.*)\s*', service_data)
	for service_status in contentToArray:
		py_shell = subprocess.Popen(["pgrep",service_status[1]], stdout=subprocess.PIPE)
	 	service_pid = re.sub(r'(\d)\n(\d)', r'\1,\2',py_shell.communicate()[0])
	 	service_pid = re.sub(r'\n', '', service_pid)
	 	if service_pid:
	 		service_pid = service_pid
	 	else:
	 		service_pid = 0
	 	if service_status[0] == "+":
	 		current_service_status = "UP"
	 	elif service_status[0] == "-":
	 		current_service_status = "DOWN"
	 	else:
	 		current_service_status = "NOT DEFINED"
	 	get_service = services.objects.filter(service_name=service_status[1])
	 	if get_service:
	 		for obj in get_service:
	 			# print "id: %s, service: %s, status: %s, time: %s" %(obj.id, obj.service_name, obj.current_status, obj.last_updated_time)	
		 		ser = services(id=obj.id, service_name=obj.service_name, current_status=current_service_status, prev_status=obj.current_status, last_updated_time=timezone.now(), pid=service_pid)
		 		ser.save(force_update=True)
		 		if current_service_status=="UP":
		 			stat = "checked"
		 		else:
		 			stat = ""
	 	else:
	 		services.objects.create(service_name=service_status[1], current_status=current_service_status, prev_status=current_service_status, pid=service_pid)
	service_list = services.objects.all()
	for obj in service_list:
		if obj.current_status=="UP":
			setattr(obj, 'stat', 'checked')	
		else:
			setattr(obj, 'stat', '')
	list_data = {
		"title": "List of Services",
		"Apps": service_list,
	}
	return list_data

def services_detail_child(request, id):
	if request.method == "POST" :
		services_update(request, id)

	instance = get_object_or_404(services, id=id) #instance = services.objects.get(id=id)
	if instance.current_status=="UP":
		setattr(instance, 'stat', 'checked')	
	else:
		setattr(instance, 'stat', '')
	list_data = {
		"header":	"Detailed Information",
		"Service_title": instance.service_name,
		"App": instance
	}
	return list_data