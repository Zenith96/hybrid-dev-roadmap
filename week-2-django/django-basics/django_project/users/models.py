from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    #WE want to have our profile a one to one relationship with the User
    user = models.OneToOneField(User,on_delete=models.CASCADE) 
    #upload_pics is the directory where we will be storing our image
    #pip insTALL Pillow to work with images
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'
