from django.db import models

# Create your models here.
from django.core import validators
# from validators import validate_email

# https://docs.djangoproject.com/en/3.0/ref/validators/
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_name(name):
    if not name.isalpha():
        raise ValidationError(
            _('%(name)s contains something other than letters'),
            params={'name': name},
        )

def validate_name_length(name):
    if len(name) < 2:
        raise ValidationError(
            _('%(name)s is less than 2 characters'),
            params={'name': name},
        )

class ZooUser(models.Model):
    first_name = models.CharField(max_length=100, validators=[validate_name,validate_name_length])
    last_name = models.CharField(max_length=100, validators=[validate_name,validate_name_length])
    email = models.EmailField(max_length=100)
    newsletter = models.BooleanField()

    def __str__(self):
        return self.last_name

# class Newsletter(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()

#     def __str__(self):
#         return self.title