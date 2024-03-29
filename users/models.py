"""
Importing models and stuff.
Don't forget to install Pillow!
"""
from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image

User = get_user_model()


class Profile(models.Model):

    """
    User profile with Image using Pillow Library
    It apparently does stuff.
    User is :model:'user' and image is :model:'image'
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):

        ## Clean previous file
        ##
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
