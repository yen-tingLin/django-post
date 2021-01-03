from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()
	date_published = models.DateTimeField(default=timezone.now)
	# ont-to-many relationship between user and posts
	# if one user is deleted, his posts wil be deleted as well
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title