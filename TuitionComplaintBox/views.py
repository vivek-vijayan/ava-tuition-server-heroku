from django.shortcuts import render, redirect
from .models import ComplaintBox
from TuitionDB.models import Student, Leader, A2Complaint_access
import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def A2C_login(request):
    return render(request, "A2C-login.html", {})

@login_required(login_url=A2C_login)
def A2P_homepage(request):
    # checking access to A2Portal
    access = A2Complaint_access.objects.filter(
        leader=request.user, valid_till__gte=datetime.datetime.now())
    if len(access) > 0:
        expire_on = access[0].valid_till
        students = Student.objects.all()
        total_students = []
        for x in students:
            total_students.append([x.student_name, x.student_id])
        return render(request, "A2C-portal.html", {'total_students': total_students, 'leader': request.user, 'expire_on': expire_on})
    else:
        return redirect(A2C_logout)


@login_required(login_url=A2C_login)
def A2P_complain_register(request):
    access = A2Complaint_access.objects.filter(
        leader=request.user, valid_till__gte=datetime.datetime.now())
    if len(access) > 0:
        complain = ComplaintBox.objects.create(
            complaint_description=request.POST['complaint'],
            student_id=request.POST['studentid'],
            student_name=request.POST['studentname'],
            category="Check-in-out-portal",
            raised_by=request.POST['leader']
        )
        complain.save()
        return redirect(A2C_display_action, username=(str(request.POST['student_name'])), action='Complain raised successfully')
    else:
        return redirect(A2C_logout)


@login_required(login_url=A2C_login)
def A2C_display_action(request, username, action):
    access = A2Complaint_access.objects.filter(
        leader=request.user, valid_till__gte=datetime.datetime.now())
    if len(access) > 0:
        return render(request, "A2C-message-display.html", {
            'username': username,
            'message': action
        })
    else:
        return redirect(A2C_logout)

def A2C_logout(request):
    logout(request)
    return redirect(A2C_login)
