from django.db import models
from django.contrib.auth.models import User
from django.db.models.aggregates import StdDev

# Create your models here.
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.ForeignKey(User, on_delete=models.CASCADE)
    student_phone_number = models.CharField(blank=True, max_length=500, default="0")
    student_class = models.IntegerField(null=True)
    date_of_joining = models.DateTimeField()
    last_date = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)
    fees = models.IntegerField(null=True)
    school = models.CharField(null=True, max_length=500)
    cbse_metric = models.CharField(null=True, max_length=500)
    dob = models.DateField(null=True)
    gender = models.CharField(null=True, max_length=200)
    emergency_contact_person = models.CharField(null=True, max_length=500)
    emergency_contact_number = models.CharField(null=True, max_length=500)
    address = models.TextField(null=True)

    def __str__(self):
        return str(self.student_id) + " -> " + str(self.student_name)

class Leader(models.Model):
    position = (
        ('Administrator', 'Administrator'),
        ('Check-in Leader', 'Check-in Leader'),
        ('File Leader', 'File Leader'),
        ('Diary Leader', 'Diary Leader')
    )
    leader_id = models.AutoField(primary_key=True)
    leader_name = models.ForeignKey(User, on_delete=models.CASCADE)
    leader_roles = models.CharField(max_length=200, choices=position)
    valid_from = models.DateTimeField(auto_now=True)
    valid_till = models.DateTimeField(null = True)
    
    def __str__(self):
        return str(self.leader_name) + " - " + str(self.leader_roles)

    # App access: 
class A2Presence_access(models.Model):
    a2p_access_id = models.AutoField(primary_key=True)
    leader = models.ForeignKey(User, on_delete=models.CASCADE)
    a2p_access = models.BooleanField(default=False)
    valid_from = models.DateTimeField(auto_now=True)
    valid_till = models.DateTimeField(null=True)
    description = models.CharField(default="bg-success", max_length=200)

    def __str__(self):
        return str(self.leader) + " - valid till : " + str(self.valid_till)


class A2Complaint_access(models.Model):
    a2c_access_id = models.AutoField(primary_key=True)
    leader = models.ForeignKey(User, on_delete=models.CASCADE)
    a2c_access = models.BooleanField(default=False)
    valid_from = models.DateTimeField(auto_now=True)
    valid_till = models.DateTimeField(null=True)
    description = models.CharField(default="bg-danger", max_length=200)

    def __str__(self):
        return str(self.leader) + " - valid till : " + str(self.valid_till)
