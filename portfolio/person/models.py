from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)

        return user


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=300)
    role = models.CharField(max_length=100)
    logo = models.CharField(max_length=500, null=True)
    tagline = models.CharField(max_length=100)
    about = models.TextField()
    description = models.TextField()
    display_image = models.CharField(max_length=300)
    skills = models.ManyToManyField("skills.Skills")
    tools = models.ManyToManyField("skills.Tools")
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
