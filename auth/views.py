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
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
	form_data = {
		"form":form,
		"title": "Home Cloud",
	}	
	return render(request, "login.html", form_data)

def auth_logout(request):
	return render(request, "login.html", {})
