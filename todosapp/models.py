
from django.db import models
import datetime
# Create your models here.
class post(models.Model):
    post=models.TextField(max_length=2000)
    date=models.DateTimeField()
