from django import forms
from django.contrib.auth import get_user_model
from user.models import Details
User = get_user_model()

class loginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={}))

	def clean_username(self):
		username = self.cleaned_data.get('username')
		qs = User.objects.filter(username=username)
		if not qs.exists():
			raise forms.ValidationError("Username invalid")
		return username

class registerForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={}))
	repassword = forms.CharField(widget=forms.PasswordInput(attrs={}))
	email = forms.CharField(widget=forms.TextInput(attrs={}))
	
	def clean(self):
		password = self.cleaned_data.get('password')
		repassword = self.cleaned_data.get('repassword')
		if not password==repassword:
			raise forms.ValidationError("Passwords must match !")
					
	
	def clean_email(self):
		email = self.cleaned_data.get('email')
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("Email already taken!")
		return email
	
	def clean_username(self):
		username = self.cleaned_data.get('username')
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("Username already taken!")
		return username

class add_details(forms.Form):
	first_name = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control"}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control"}))
	address = forms.CharField(widget=forms.Textarea(attrs={"class" : "form-control"}))
	age = forms.IntegerField(widget=forms.NumberInput(attrs={"class" : "form-control"}))
	aadhar_id = forms.IntegerField(widget=forms.NumberInput(attrs={"class" : "form-control"}))
	disablity = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control"}))
	category = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control"}))
	percentage_disabliity = forms.DecimalField(widget=forms.NumberInput(attrs={"class" : "form-control"}))
	ward = forms.IntegerField(widget=forms.NumberInput(attrs={"class" : "form-control"}))
	house = forms.IntegerField(widget=forms.NumberInput(attrs={"class" : "form-control"}))
	village = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control"}))
	education = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control"}))
	job = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control"}))
	income = forms.DecimalField(widget=forms.NumberInput(attrs={"class" : "form-control"}))

	def clean_aadhar_id(self):
		aadhar_id = self.cleaned_data.get('aadhar_id')
		qs = Details.objects.filter(aadhar_id=aadhar_id)
		if qs.exists():
			raise forms.ValidationError("Aadhar ID already registered!")
		return aadhar_id