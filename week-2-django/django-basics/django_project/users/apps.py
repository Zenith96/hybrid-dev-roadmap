from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
     #If you wanna set up signals, monkey patches, or anything you want
     #  to run once when the app loads — put it here.
    def ready(self):
       import users.signals