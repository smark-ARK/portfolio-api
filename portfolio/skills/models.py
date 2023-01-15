from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Skills(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=300)
    proficiency=models.IntegerField()

class Tools(models.Model):
    id=models.AutoField(primary_key=True)
    name=ArrayField(models.CharField(max_length=300))
    skill_id=models.ForeignKey(Skills,on_delete=models.CASCADE)
