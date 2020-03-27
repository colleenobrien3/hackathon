from django.db import models

# Create your models here.

class ZooUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    newsletter = models.BooleanField()

    def __str__(self):
        return self.last_name

# class Newsletter(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()

#     def __str__(self):
#         return self.title