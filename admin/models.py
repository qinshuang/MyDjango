from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserInfo(User):
    sex = models.BooleanField(default=True)
    notes = models.CharField(default='', max_length=200)
    picture = models.CharField(default='', max_length=200)
