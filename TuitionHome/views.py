from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from TuitionDB.models import A2Presence_access, Student, Leader
from TuitionAttendance.models import Check_in_out_register
# Create your views here.
import datetime


def AVA_login(request):
    if request.user.is_authenticated:
        return render(request, "AVA-login-message-display.html", {'username': request.user, 'message': "Authenticated successfully"})
    else:
        return render(request, "AVA-login.html", {})


def AVA_logginer(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user:
        if user:
            login(request, user)
            return render(request, "AVA-login-message-display.html", {'username': request.user, 'message': "Login successful"})
        # checking access to A2Portal
        
    else:
        return render(request, "AVA-login.html", {'error': 'Invalid credentials', 'iserror': True})


@login_required(login_url=AVA_login)
def AVA_Home(request):
    if request.user.is_superuser:
        a2p_access = True
        fullname = str(request.user.first_name) + \
            " " + str(request.user.last_name)
        return render(request, "AVA-home.html", {
            'username': request.user,
            'fullname': fullname,
            'firstname': request.user.first_name,
            'fees': "Administrator",
            'a2p_access' : a2p_access,
            'show_stat' : False,
        })
    elif request.user.is_active:
        # A2Presence access check
        a2p = A2Presence_access.objects.filter(leader=request.user)
        a2p_access = True if len(a2p) > 0 else False 
        entry = Check_in_out_register.objects.filter(
            student_name=request.user, attendance_date=datetime.date.today(), raised_absent = True)
        absent = True if len(entry) > 0 else False
        entry = Check_in_out_register.objects.filter(
            student_name=request.user, attendance_date=datetime.date.today())
        status = entry[0].status if len(entry) > 0 else "Not Arrived"
        if len(entry)  > 0:
            check_in_time = entry[0].in_time
            check_out_time = entry[0].out_time
            day_off = entry[0].day_off
        else:
            check_in_time = None
            check_out_time = None
            day_off = False
        student = Student.objects.filter(student_name=request.user, is_active=True)
        leader = Leader.objects.filter(leader_name = request.user)
        if len(leader) > 0:
            is_leader = True
            leader_roles = leader[0].leader_roles
        else:
            is_leader =False
            leader_roles = ""
        if len(student) > 0:
            fullname = str(request.user.first_name) + \
                " " + str(request.user.last_name)
            return render(request, "AVA-home.html", {
                'username': request.user,
                'fullname': fullname,
                'firstname': request.user.first_name,
                'fees': "Fees ₹ " + str(student[0].fees),
                'a2p_access': a2p_access,
                'date_of_joining': student[0].date_of_joining,
                'is_leader': is_leader,
                'leader_roles' : leader_roles,
                'absent': absent,
                'show_stat' : True,
                'status': status,
                'day_off' :day_off,
                'check_in_time' : check_in_time,
                'check_out_time': check_out_time
            })
        else:
            return render(request, "AVA-Error.html", {'username': request.user, 'message': "Your account has been locked"})
    else:
        return render(request, "AVA-Error.html", {'username': request.user, 'message': "Your account has been locked"})


@login_required(login_url=AVA_login)
def AVA_A2P_self_absent_request(request):
    return render(request, "RaiseSelfAbsentConfirmation.html", {
        'username' : request.user
    })


@login_required(login_url=AVA_login)
def AVA_A2P_self_absent_apply(request):
    student = Student.objects.get(
        student_name__username__contains=request.POST['username'])
    entry = Check_in_out_register.objects.create(
        student_name=student.student_name, status="Absent", raised_absent=True, day_off=True)
    entry.save()
    return render(request, "AVA-message-display.html", {'username': request.user, 'message': "Leave applied successfully"})


def AVA_logout(request):
    logout(request)
    return redirect(AVA_login)
