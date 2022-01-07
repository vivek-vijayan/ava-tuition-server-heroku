from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class ComputerClassRegistration(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    fees = models.IntegerField()
    class_description = models.TextField()
    joining_date = models.DateField()
    end_date = models.DateField(default=datetime.datetime.now())
