from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bg_color = models.CharField(max_length=7, null=True, blank=True, help_text="Hexadecimal background color", default='#c8d4fd')
    bg_image = models.ImageField(upload_to='background_images/', null=True, blank=True, help_text="Background image")
    image_resize = models.BooleanField(default=False)
