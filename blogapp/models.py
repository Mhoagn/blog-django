from django.db import models

# Create your models here.

class TestConnection(models.Model):
    name = models.CharField(max_length=100)