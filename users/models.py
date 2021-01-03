from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
	# if one user is deleted, his profile will be deleted as well;
	# but if the profile is deleted, the user won't be deleted
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	# each profile has a default image
	image = models.ImageField(default='default.jpg', upload_to='profile_pic')

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
		super().save(force_insert, force_update, using, update_fields)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)


