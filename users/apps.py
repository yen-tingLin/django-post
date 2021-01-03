from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # for User instance and its profile
    def ready(self):
    	import users.signals
