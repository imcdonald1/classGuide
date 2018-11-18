from django.shortcuts import render
from django.http import HttpResponseRedirect
from login.models import User
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import createReviewForm, searchReviews
from datetime import date
# Create your views here.
@login_required
def home(request):

	if request.method == 'GET':
		currentUserID = request.user.id
		reviews = Review.objects.filter(userID=currentUserID)
		
		return render(request, 'reviews/home.html', {'username': request.user.username,
			'reviews': reviews})

	return render(request, 'reviews/home.html', {'username': request.user.username})


@login_required
def createReview(request):
	if request.method == 'POST':
		form = createReviewForm(request.POST)
		form.is_valid()
		
		today = str(date.today())
		newReview =  Review(userID=request.user.id, reviewDate=today, termTaken=form.cleaned_data['termTaken'],
							className=form.cleaned_data['className'], courseNum=form.cleaned_data['courseNum'],
							courseSubject=form.cleaned_data['courseSubject'], school=form.cleaned_data['school'],
							review=form.cleaned_data['review'], teacherName=form.cleaned_data['teacherName'],
							reviewerName=request.user.username)
		newReview.save()
		return HttpResponseRedirect('/home/')
	
	else:
		form = createReviewForm()
	
	return render(request, 'reviews/createReview.html', {'form': form})

def reviewSearch(request):
	if request.method == 'POST':
		#comeplete search and render search results
		form = searchReviews(request.POST)
		form.is_valid()
		x = None
		if form.has_changed():
			x = Review.objects.all()
			if 'className' in form.changed_data:
				x = x.filter(className=form.cleaned_data['className'])
			if 'courseNum' in form.changed_data:
				x = x.filter(courseNum=form.cleaned_data['courseNum'])
			if 'courseSubject' in form.changed_data:
				x = x.filter(courseSubject=form.cleaned_data['courseSubject'])
			if 'school' in form.changed_data:
				x = x.filter(school=form.cleaned_data['school'])
				
		return render(request, 'reviews/results.html', {'results': x})
	else:
		form = searchReviews()

	return render(request, 'reviews/search.html', {'form': form})

def serchRedirect(request):
	return HttpResponseRedirect('/reviewSearch/')