from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    created = models.DateField(auto_created=True, null=True)
    last_update = models.DateField(auto_now_add=True, null=True)


class Notes(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='notes')
    note_title = models.CharField(max_length=500)
    note_content = models.CharField(max_length=1000)
    created_on = models.DateField(auto_created=True)
    updated_on = models.DateTimeField(auto_now_add=True)
