from django.db import models

# Create your models here.

class Login(models.Model):
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=122)

    def __str__(self) -> str:
        return self.email

class DataBasePass(models.Model):
    website = models.TextField()
    emailtosave = models.CharField(max_length=122)
    passwordtosave = models.CharField(max_length=122)
    name = models.CharField(max_length=122)

    def __str__(self) -> str:
        return self.website