from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# When a user is saved(registered), sends a signal to receiver 
@receiver(post_save,sender=User)
#The receiver creates create_profile
def create_profile(sender , instance , created , **kwargs):
    if created:
        Profile.objects.create(user=instance)


# When a user is saved, send the signal to receiver 
@receiver(post_save,sender=User)
#The receiver creates save_profile
def save_profile(sender , instance  , **kwargs):
    instance.profile.save()