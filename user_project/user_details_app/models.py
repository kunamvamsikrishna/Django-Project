from django.db import models

class UserDetails(models.Model):
             username = models.CharField(max_length=150,unique=True)
             gender = models.CharField()
             age = models.IntegerField()