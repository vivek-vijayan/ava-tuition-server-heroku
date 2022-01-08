from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Month(models.Model):
    month = models.CharField(primary_key=True, max_length=200)

    def __str__(self) -> str:
        return self.month

class FeesCollector(models.Model):

    PAYMENT_MODE = [
        ('CASH', 'CASH'),
        ('UPI', 'UPI'),
        ('CARD', 'CARD'),
    ]

    student = models.ForeignKey(User, on_delete=models.PROTECT)
    fees = models.IntegerField()
    paid_month = models.ForeignKey(Month, on_delete=models.PROTECT)
    paid_year = models.IntegerField()
    late_pay = models.BooleanField(default=False)
    late_pay_fine = models.IntegerField(default=0)
    payment_on = models.DateTimeField(auto_now=True)
    paid_for = models.CharField(max_length=200)
    payment_mode = models.CharField(max_length=200, choices=PAYMENT_MODE, default="CASH")

    def __str__(self) -> str:
        return str(self.student) + " Paid: Rs." + str(int(self.fees) + int(self.late_pay_fine)) + " - PERIOD : " + str(self.paid_month) + " " + str(self.paid_year) 
