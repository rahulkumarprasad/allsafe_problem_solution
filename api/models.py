from django.db import models

# Create your models here.
class AllsafeWebsite(models.Model):
    status=models.IntegerField()
    total_request=models.BigIntegerField(default=0)
    time=models.TimeField(auto_now=True)
    date=models.DateField(auto_now_add=True)