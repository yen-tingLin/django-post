from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# signal :  post_save
# signal sender : User
# signal receiver : create_profile()
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	# if instance of user is created
	if created:
		# create a profile for that instance of user
		Profile.objects.create(user=instance)


def save_profile(sender, instance, **kwargs):
	# instance : the User
	instance.profile.save()