from django.db import models
from django.conf import settings


class Course(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="courses"
    )

    name = models.CharField(max_length=100)

    professor = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
