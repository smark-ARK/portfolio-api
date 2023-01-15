from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Projects(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=300)
    short_description=models.TextField()
    tech_used=ArrayField(models.CharField(max_length=200))
    detail_description=models.TextField()
    github_link=models.CharField(max_length=300)
    deploy_link=models.CharField(max_length=300)
    collaborators=ArrayField(models.CharField(max_length=200))
    video_explaination=models.CharField(max_length=300,null=True)
    display_image=models.CharField(max_length=300,null=True)
    all_images=ArrayField(models.CharField(max_length=300))

