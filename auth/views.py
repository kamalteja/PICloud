from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import (
	authenticate, 
	login, 
	logout,
	)
from .forms import UserLoginForm

# Create your views here.
def auth_login(request):
	print(request.user.is_authenticated())
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request, user)
		print(request.user.is_authenticated())
		#redirect
	form_data = {
		"form": form,
		"title": "Home Cloud",
		"authStatus": request.user.is_authenticated(), 
	}	
	return render(request, "login.html", form_data)

def auth_logout(request):
	logout(request)
	return render(request, "login.html", {})

def auth_warn(request):
	return HttpResponse("<h1>Intruder</h1>")