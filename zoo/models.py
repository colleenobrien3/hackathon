from django.db import models

# Create your models here.

class ZooUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    newsletter = models.BooleanField()

    def __str__(self):
        return self.name

# class Newsletter(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()

#     def __str__(self):
#         return self.title