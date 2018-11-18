from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(label='password', max_length=20)

class createUserForm(forms.Form):
	username = forms.CharField(label='Username', max_length=20)
	password = forms.CharField(label='password', max_length=20)
	email = forms.CharField(label='email', max_length=20)
	first_name = forms.CharField(label='first_name', max_length=20)
	last_name = forms.CharField(label='last_name', max_length=20)
