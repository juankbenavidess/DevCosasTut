from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


# Create your models here.

class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    modified = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(null=True, upload_to='users')
    extract = RichTextField(null=True)
    phone = models.CharField(null=True, max_length=15)
    city = models.CharField(null=True, max_length=255)
    country = models.CharField(null=True, max_length=255)
    is_recruiter = models.BooleanField(default=False)
