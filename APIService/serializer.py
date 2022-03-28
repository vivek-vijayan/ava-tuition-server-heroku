from dataclasses import fields
from rest_framework import serializers
from TuitionDB.models import Student
from django.contrib.auth.models import User

class StudentsAPI(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class UserAPI(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"