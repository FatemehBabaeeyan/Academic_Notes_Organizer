from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(
        User,on_delete=models.CASCADE,related_name="profile")
    student_id = models.CharField(max_length=20, unique=True)

    