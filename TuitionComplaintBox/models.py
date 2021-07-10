from django.db import models

# Create your models here.


class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True, default=None)
    complaint_description = models.TextField(blank=True)
    student_id = models.IntegerField(default=0)
    student_name = models.CharField(blank=True, max_length=255)
    raised_on = models.DateTimeField(auto_now=True)
    category = models.CharField(blank=True, max_length=255)
    raised_by = models.CharField(max_length=255)
    resolved = models.BooleanField(default=False)
