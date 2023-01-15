from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    role = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100)
    about = models.TextField()
    description = models.TextField()
    display_image = models.CharField(max_length=300)
