from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Check_in_out_register(models.Model):
    entry_id = models.AutoField(primary_key=True, default= None)
    student_name = models.ForeignKey(User, on_delete=models.CASCADE)
    attendance_date = models.DateField(auto_now=True)
    day_off = models.BooleanField(default=False)
    in_time = models.DateTimeField(null=True)
    out_time = models.DateTimeField(null=True)
    status = models.CharField(max_length=200, default="Not Arrived")
    raised_absent = models.BooleanField(default=False)
