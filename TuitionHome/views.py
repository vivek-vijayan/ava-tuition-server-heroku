from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from TuitionDB.models import A2Presence_access, Student, Leader
from TuitionAttendance.models import Check_in_out_db_register
from django.contrib.auth.models import User
# Create your views here.
import datetime


def AVA_login(request):
    if request.user.is_authenticated:
        return render(request, "AVA-login-message-display.html", {'username': request.user, 'message': "Authenticated successfully"})
    else:
        return render(request, "AVA-login.html", {})


@login_required(login_url=AVA_login)
def AVA_password_reset(request):
    access_to_change_password = User.objects.filter(username=request.user, is_staff=True, is_active=True)
    if len(access_to_change_password) > 0:
        return render(request, "AVA-password-change.html", {'username': request.user})
    else:
        return render(request, "AVA-Error2.html", {'username': request.user, 'message': "Password change option has been locked by administrator"})


@login_required(login_url=AVA_login)
def AVA_change_password(request):
    new_password = request.POST['new_password']
    repeat_password = request.POST['repeat_password']
    access_to_change_password = User.objects.filter(
        username=request.user, is_staff=True, is_active=True)
    if len(access_to_change_password) > 0:
        if new_password == repeat_password:
            access_to_change_password[0].set_password(new_password)
            access_to_change_password[0].save()
            return render(request, "AVA-message-display.html", {
                'username': request.user,
                'message': "Password has been reset successfully"
            })
        else:
            return render(request, "AVA-password-change.html", {
                'username' : request.user,
                'is_error' : True,
                'error': "Old password is correct"
            })

    else:
        return render(request, "AVA-Error2.html", {'username': request.user, 'message': "Password change option has been locked by administrator"})




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
        fullname = str(request.user.first_name)
        return render(request, "AVA-home.html", {
            'username': request.user,
            'fullname': fullname,
            'firstname': request.user.first_name,
            'fees': "Administrator",
            'a2p_access' : a2p_access,
            'show_stat' : False,
            'is_leader': True,
            'logo' : request.user.last_name,
            'leader_roles': "Administrator",
        })
    elif request.user.is_active:
        # A2Presence access check
        a2p = A2Presence_access.objects.filter(
            leader=request.user, valid_till__gte=datetime.datetime.now())
        a2p_access = True if len(a2p) > 0 else False 
        entry = Check_in_out_db_register.objects.filter(
            student_name=request.user, attendance_date=datetime.date.today(), raised_absent = True)
        absent = True if len(entry) > 0 else False
        entry = Check_in_out_db_register.objects.filter(
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
        leader = Leader.objects.filter(
            leader_name=request.user, valid_till__gte=datetime.datetime.now())
        if len(leader) > 0:
            is_leader = True
            leader_roles = leader[0].leader_roles
        else:
            is_leader =False
            leader_roles = ""
        
        if len(student) > 0:
            fullname = str(request.user.first_name) 
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
                'check_out_time': check_out_time,
                'logo': request.user.last_name,
                'class':student[0].student_class
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
    entry = Check_in_out_db_register.objects.create(
        student_name=student.student_name, status="Absent", raised_absent=True, day_off=True)
    entry.save()
    return render(request, "AVA-message-display.html", {'username': request.user, 'message': "Leave applied successfully"})


def AVA_logout(request):
    logout(request)
    return redirect(AVA_login)

def show_leader(request, user_id):
    leader = Leader.objects.filter(
        leader_name__username__contains=user_id, valid_till__gte=datetime.datetime.now())
    name = User.objects.filter(username=user_id, is_active=True)
    if len(name)>0:
        if len(leader) > 0:
            return render(request, "Leader.html", {
                'leader' : leader[0].leader_name,
                'photo' : name[0].last_name,
                'role' : leader[0].leader_roles,
                'valid' : True,
                'end': leader[0].valid_till
            })
        
        else:
            return render(request, "LeaderNo.html", {
                'leader': user_id,
                'photo': name[0].last_name,
            })
    else:
        return render(request, "AVA-Error2.html", {'username': user_id, 'message': "Leader account has been de-activated"})
