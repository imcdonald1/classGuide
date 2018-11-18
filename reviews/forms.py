from django import forms

class createReviewForm(forms.Form):
	termTaken = forms.CharField(label='termTaken', max_length=20)
	className = forms.CharField(label='class Name', max_length=20)
	courseNum = forms.CharField(label='courseNum', max_length=20)
	courseSubject = forms.CharField(label='courseSubject', max_length=50)
	school = forms.CharField(label='school', max_length=50)
	review = forms.CharField(label='review', max_length=500)
	teacherName = forms.CharField(label='teacherName', max_length=30)

class searchReviews(forms.Form):
	className = forms.CharField(label='class Name', max_length=20, initial='Class Name')
	courseNum = forms.CharField(label='courseNum', max_length=20, initial='Course Number')
	courseSubject = forms.CharField(label='courseSubject', max_length=50, initial='Course Subject')
	school = forms.CharField(label='school', max_length=50, initial='School')