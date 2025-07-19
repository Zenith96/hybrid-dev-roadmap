from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    #WE want to have our profile a one to one relationship with the User
    user = models.OneToOneField(User,on_delete=models.CASCADE) 
    #upload_pics is the directory where we will be storing our image
    #pip insTALL Pillow to work with images
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'
    #We will be adding our requirements after saving 
    # in the pre built save method of models 
    def save(self,*args,**kwargs):
        #Run save method of parent class
        super().save(*args,**kwargs)

        img =  Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)




