from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def auth_login(request):
	return render(request, "login.html")