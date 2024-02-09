from django.db import models

class todos(models.Model):
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
