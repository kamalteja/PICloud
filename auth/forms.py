from django import forms
from django.contrib.auth import (
	authenticate, 
	login, 
	logout,
	)


class UserLoginForm(forms.Form):
	"""This class contains the text fields related to login"""
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		print user
		if not user:
			raise forms.ValidationError("This user does not exists")
		if not user.check_password(password):
			raise forms.ValidationError("incorrect password")
		if not user.is_active:
			raise forms.ValidationError("This user is not active")
		return super(UserLoginForm, self).clean(*args, **kwargs)