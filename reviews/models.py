from django.db import models

# Create your models here.
class Review(models.Model):
	userID = models.IntegerField()
	reviewDate = models.DateField()
	termTaken = models.TextField()
	className = models.TextField()
	courseNum = models.TextField()
	courseSubject = models.TextField()
	school = models.TextField()
	review = models.TextField()
	teacherName = models.TextField()
	reviewerName = models.TextField(default='anon')
