from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializer import StudentsAPI, UserAPI
from TuitionDB.models import Student
from django.contrib.auth.models import User

class getAllStudents(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentsAPI

class getAllUsers(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserAPI