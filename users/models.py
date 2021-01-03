from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	# if one user is deleted, his profile will be deleted as well;
	# but if the profile is deleted, the user won't be deleted
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	# each profile has a default image
	image = models.ImageField(default='default.jpg', upload_to='profile_pic')

	def __str__(self):
		return f'{self.user.username} Profile'
