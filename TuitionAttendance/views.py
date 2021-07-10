from django.shortcuts import render, redirect
from TuitionDB.models import Student, Leader, A2Presence_access
from TuitionAttendance.models import Check_in_out_register
from TuitionComplaintBox.models import Complaint
import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

# A2Portal   -------------------------------------------

def A2P_login(request):
    return render(request, "A2P-login.html", {})

def A2P_logginer(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user:
        # checking access to A2Portal
        access = A2Presence_access.objects.filter(
            leader=user, valid_till__gte=datetime.datetime.now())
        if len(access) > 0:
            login(request, user)
            return redirect(A2P_homepage)
        else:
            return render(request, "A2P-login.html", {'error': 'A2Portal access expired, contact admin', 'iserror': True})
    else:
        return render(request, "A2P-login.html", {'error': 'Invalid credentials', 'iserror': True})

@login_required(login_url=A2P_login)
def A2P_homepage(request):
    # checking access to A2Portal
    access = A2Presence_access.objects.filter(
        leader=request.user, valid_till__gte=datetime.datetime.now())
    if len(access) > 0:
        expire_on = access[0].valid_till 
        students = Student.objects.all()
        total_students = []
        for x in students:
            total_students.append([x.student_name, x.student_id])
        return render(request, "A2P-portal.html", {'total_students': total_students, 'leader': request.user, 'expire_on': expire_on})
    else:
        return redirect(A2P_logout)

@login_required(login_url=A2P_login)
def A2P_query(request):
    access = A2Presence_access.objects.filter(
        leader=request.user, valid_till__gte=datetime.datetime.now())
    
    if len(access) > 0:
        expire_on = access[0].valid_till
        checkedIn = False
        # checking the status
        try:
            entry = Check_in_out_register.objects.filter(
                student_id=request.POST['student_name_selection'], attendance_date=datetime.date.today())
            checkedIn = True
            complain = Complaint.objects.filter(
                student_id=request.POST['student_name_selection'], 
                category="Check-in-out-portal",
                resolved = False
                )
            complain_count = 0
            for x in complain:
                complain_count = complain_count + 1
            students = Student.objects.all()
            total_students = []
            queryStudent = request.POST['student_name_selection']
            student = Student.objects.get(student_id=queryStudent)
            for x in students:
                total_students.append([x.student_name, x.student_id])
            return render(request, "A2P-portal-student.html", {
                'total_students': total_students,
                'studentname': student.student_name,
                'studentid' : student.student_id,
                'status': entry[0].status,
                'check_in_time': entry[0].in_time,
                'check_out_time' : entry[0].out_time,
                'day_off': entry[0].day_off,
                'leader': request.user,
                'total_complain': complain_count,
                'expire_on': expire_on
            })
        except:
            checkedIn = False
            students = Student.objects.all()
            total_students = []
            queryStudent = request.POST['student_name_selection']
            student = Student.objects.get(student_id=queryStudent)
            for x in students:
                total_students.append([x.student_name, x.student_id])
            return render(request, "A2P-portal-student.html", {
                'total_students': total_students,
                'studentname': student.student_name,
                'studentid': student.student_id,
                'status' : 'Not Arrived',
                'leader': request.user,
                'expire_on': expire_on
                })
    else:
        return redirect(A2P_logout)


@login_required(login_url=A2P_login)
def A2P_checkin(request):
    access = A2Presence_access.objects.filter(
        leader=request.user, valid_till__gte=datetime.datetime.now())
    if len(access) > 0:
        # Entry Creation
        entry = Check_in_out_register.objects.create(
            student_id=request.POST['student_id'], status="Checked In")
        entry.save()
        return redirect(A2P_display_action, username = (str(request.POST['student_name'])), action = 'Checked In successfully')
    else:
        return redirect(A2P_logout)



@login_required(login_url=A2P_login)
def A2P_checkout(request):
    access = A2Presence_access.objects.filter(
        leader=request.user, valid_till__gte=datetime.datetime.now())
    if len(access) > 0:
        entry = Check_in_out_register.objects.filter(
            student_id=request.POST['student_id'], attendance_date=datetime.date.today()).update(out_time=datetime.datetime.now())
        entry = Check_in_out_register.objects.filter(
            student_id=request.POST['student_id'], attendance_date=datetime.date.today()).update(status="Checked Out")
        entry = Check_in_out_register.objects.filter(student_id=request.POST['student_id'], attendance_date=datetime.date.today()).update(day_off=True)
        return redirect(A2P_display_action, username=(str(request.POST['student_name'])), action='Checked out successfully')
    else:
        return redirect(A2P_logout)



@login_required(login_url=A2P_login)
def A2P_display_action(request, username, action):
    access = A2Presence_access.objects.filter(
        leader=request.user, valid_till__gte=datetime.datetime.now())
    if len(access) > 0:
        return render(request, "A2P-message-display.html", {
            'username' : username,
            'message' : action
        })
    else:
        return redirect(A2P_logout)


def A2P_logout(request):
    logout(request)
    return redirect(A2P_login)

