from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class LastExaminationScoreOut(models.Model):
    exam_id = models.AutoField(primary_key=True)
    exam_title = models.CharField(max_length=200)
    max_mark = models.IntegerField(null=True)

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    show_ld = models.DateTimeField()

    english_mark = models.IntegerField(default = 0)
    is_english = models.BooleanField(default=True)

    tamil_mark = models.IntegerField(default = 0)
    is_tamil = models.BooleanField(default=True)

    science_mark = models.IntegerField(default = 0)
    is_science = models.BooleanField(default=True)

    social_mark = models.IntegerField(default = 0)
    is_social = models.BooleanField(default=True)

    maths_mark = models.IntegerField(default = 0)
    is_maths = models.BooleanField(default=True)

    computer_mark = models.IntegerField(default = 0)
    is_computer = models.BooleanField(default=True)

    total_mark = models.IntegerField(default = 0)


    def __str__(self):
        return str(self.student) + " --> " +  str(self.exam_title) + "  Total = "+ str(self.total_mark)