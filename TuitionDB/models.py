from django.db import models
from django.contrib.auth.models import User
from django.db.models.aggregates import StdDev

# Create your models here.
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=20)
    student_phone_number = models.IntegerField(null=True)
    student_class = models.IntegerField(null=True)
    date_of_joining = models.DateTimeField()
    fees = models.IntegerField(null=True)

    def __str__(self):
        return str(self.student_id) + " -> " + str(self.student_name)

class Leader(models.Model):
    position = (
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
class A2Portal_access(models.Model):
    a2p_access_id = models.AutoField(primary_key=True)
    leader = models.ForeignKey(User, on_delete=models.CASCADE)
    a2p_access = models.BooleanField(default=False)
    valid_from = models.DateTimeField(auto_now=True)
    valid_till = models.DateTimeField(null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return str(self.leader) + " - valid till : " + str(self.valid_till)