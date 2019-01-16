from django import forms
from django.contrib.auth.models import User
from .models import Visitor,Room,Booking

class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ['first_name','last_name','email','username','password']

class VisitorForm(forms.ModelForm):
	class Meta:
		model = Visitor
		fields = ['phone_no','address']

class RoomsForm(forms.Form):

	from_date = forms.DateField(widget = forms.SelectDateWidget())
	to_date = forms.DateField(widget = forms.SelectDateWidget())

		
