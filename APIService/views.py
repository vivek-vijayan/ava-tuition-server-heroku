from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializer import StudentsAPI
from TuitionDB.models import Student

class show_student(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentsAPI
