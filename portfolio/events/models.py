from django.db import models
from django.contrib.postgres.fields import ArrayField




class Events(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    display_image=models.CharField(max_length=300,null=True)
    all_image=ArrayField(models.CharField(max_length=300,null=True))
    description=models.TextField()

# Create your models here.
