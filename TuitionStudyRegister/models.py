from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class StudyRegister(models.Model):
    entry_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    study_date = models.DateField(auto_now=True)
    subject = models.CharField(blank=True, max_length=200)
    description = models.TextField(blank=True)
    study_time = models.DateTimeField(auto_now=True)
    status = models.CharField(blank=True, max_length=200)

