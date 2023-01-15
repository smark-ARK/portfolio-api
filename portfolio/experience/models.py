from django.db import models
from django.contrib.postgres.fields import ArrayField


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    company_name=models.CharField(max_length=200)
    website=models.CharField(max_length=300)



class Experience(models.Model):
    id = models.AutoField(primary_key=True)
    role=models.CharField(max_length=200)
    level=models.CharField(max_length=300)
    description=models.TextField()
    stack=ArrayField(models.CharField(max_length=100))
    company_id=models.ForeignKey(Company,on_delete=models.CASCADE)


# Create your models here.
