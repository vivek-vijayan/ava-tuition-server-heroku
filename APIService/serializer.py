from dataclasses import fields
from rest_framework import serializers
from TuitionDB.models import Student
from django.contrib.auth.models import User

class StudentsAPI(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"