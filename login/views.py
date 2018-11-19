from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserForm, createUserForm
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.
def loginPage(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		form.is_valid()
		tempUser = User.objects.get(username=form.cleaned_data['username'])
		user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
		if user is not None:
			login(request, user)
			request.session['member_id'] = user.id
			return HttpResponseRedirect('/home/')

	else:
		form = UserForm()

	if request.user.is_authenticated:
		return HttpResponseRedirect('/home/')

	return render(request, 'login/login.html', {'form': form})


def createUser(request):
	if request.method == 'POST':
		form = createUserForm(request.POST)
		form.is_valid()
		newUser =  User(username=form.cleaned_data['username'], password=form.cleaned_data['password'], 
						email=form.cleaned_data['email'], first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'])
		newUser.save()
		return HttpResponseRedirect('/loginPage/')
	
	else:
		form = createUserForm()
	
	return render(request, 'login/createUser.html', {'form': form})

def createUserRedirect(request):
	return HttpResponseRedirect('/createUser/')

def logoutPage(request):
	logout(request)
	return render(request, 'login/logout.html')