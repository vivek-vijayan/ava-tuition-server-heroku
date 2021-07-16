from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from TuitionDB.models import Student, Leader, A2Study_access
from TuitionAttendance.models import Check_in_out_db_register
from TuitionComplaintBox.models import ComplaintBox
import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import StudyRegister


def A2S_login(request):
    return redirect('/')


def A2S_logout(request):
    logout(request)
    return redirect('/')


@login_required(login_url=A2S_login)
def A2S_Student_Home(request):
    students = Student.objects.filter(is_active=True, last_date__gte=datetime.datetime.now())
    total_students = []
    temp = None
    for x in students:
        name = User.objects.filter(username=x.student_name, is_active=True)
        study_reg = StudyRegister.objects.filter(
            student=x.student_name, study_date=datetime.date.today())
        if len(study_reg) > 0:
            temp = study_reg.status
        else:
            temp = "Not Studied"
        total_students.append([x.student_name, name[0].first_name, temp])

    if request.user.is_superuser:
        leader_check = A2Study_access.objects.filter(leader = request.user, valid_till__gte = datetime.datetime.now())
        if len(leader_check) > 0:
            return render(request, "A2S-student-portal.html", {'role': 'Administrator', 'total_students': total_students})
            
    if request.user.is_active:
        leader_check = A2Study_access.objects.filter(
            leader=request.user, valid_till__gte=datetime.datetime.now())
        if len(leader_check) > 0:
            teacher = Leader.objects.filter(
                leader_name=request.user, valid_till__gte=datetime.datetime.now(), leader_roles="Teacher")
            if len(teacher) > 0:
                return render(request, "A2S-student-portal.html", {'role': 'Teacher'})
            student = Student.objects.filter(
                student_name=request.user, is_active=True, last_date__gte=datetime.datetime.now())

        # Suudents work
        if len(student) > 0:
            return render(request, "A2S-student-portal.html", {'role': 'Student'})
        else:
            return render(request, "AVA-Error2.html", {'username': request.user, 'message': "Leader account has been de-activated"})


def A2S_Study_Register(request):
    return render(request, "A2S-student-portal.html", {})
