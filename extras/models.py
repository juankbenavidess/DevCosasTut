from django.db import models
from users.models import User

from ckeditor.fields import RichTextField


class Extra(models.Model):
    """Extra model"""
    user = models.ForeignKey(User, models.CASCADE)
    expedition = models.DateTimeField()
    title = models.CharField(max_length=255)
    url = models.URLField(null=True)
    description = RichTextField(null=True)

    def __str__(self):
        """Return extra academic education, first_name and last_name"""
        return f'{self.user.first_name} {self.user.last_name} | {self.title}'
