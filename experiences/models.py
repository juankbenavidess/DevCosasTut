from django.db import models
from users.models import User

from ckeditor.fields import RichTextField


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_ini = models.DateTimeField()
    date_end = models.DateTimeField(null=True)
    company = models.CharField(max_length=255)
    description = RichTextField()

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} | {self.company}'
