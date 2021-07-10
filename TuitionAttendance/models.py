from django.db import models

# Create your models here.

class Check_in_out_register(models.Model):
    entry_id = models.AutoField(primary_key=True, default= None)
    student_id = models.IntegerField(null=True)
    attendance_date = models.DateField(auto_now=True)
    day_off = models.BooleanField(default=False)
    in_time = models.DateTimeField(auto_now=True)
    out_time = models.DateTimeField(null=True)
    status = models.CharField(max_length=200, default="Not Arrived")
    
