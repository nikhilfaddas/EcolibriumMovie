from django.db import models

# Create your models here.

class Movies(models.Model):
    mName = models.CharField(max_length=50)
    mRdate = models.DateField()
    mLang = models.CharField(max_length=80)