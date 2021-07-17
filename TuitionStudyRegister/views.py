from django.http.response import HttpResponse
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
from django.db.models import Q

def A2S_login(request):
    return redirect('/')


def A2S_logout(request):
    logout(request)
    return redirect('/')


@login_required(login_url=A2S_login)
def A2S_Detail(request):
    username = request.POST['username']
    study_reg = StudyRegister.objects.filter(student__username__contains = username, study_date=datetime.date.today())
    user = User.objects.filter(
        username = study_reg[0].student,
    )
    return render(request, "A2S-student-portal-detail.html", {
        'studentname' : user[0].username,
        'studytime' : study_reg[0].study_time,
        'studydate' : study_reg[0].study_date,
        'subject' : study_reg[0].subject,
        'desc' : study_reg[0].description,
        'studentimage' : user[0].last_name,
        'leadername' : request.user,
        'approved' : study_reg[0].approved_by_trainer,
        'declined': study_reg[0].declined_by_trainer,
        'by' : study_reg[0].actioned_by
    })

@login_required(login_url=A2S_login)
def A2S_Home(request):
    students = Student.objects.filter(is_active=True, last_date__gte=datetime.datetime.now())
    total_students = []
    temp = None
    for x in students:
        name = User.objects.filter(username=x.student_name, is_active=True)
        study_reg = StudyRegister.objects.filter(
            student__username__contains=x.student_name, study_date=datetime.date.today())
        approved = declined = None
        if len(study_reg) > 0:
            temp = study_reg[0].status
            approved = study_reg[0].approved_by_trainer
            declined = study_reg[0].declined_by_trainer
        else:
            temp = "Not Studied"

        total_students.append([x.student_name, name[0].first_name, temp, approved, declined])

    if request.user.is_superuser:
        leader_check = A2Study_access.objects.filter(leader = request.user, valid_till__gte = datetime.datetime.now())
        if len(leader_check) > 0:
            return render(request, "A2S-student-portal.html", {'role': 'Administrator', 'total_students': total_students, 'leader': request.user, 'expire_on': leader_check[0].valid_till})
        else:
            return render(request, "AVA-Error2.html", {'username': request.user, 'message': "No Access to this portal"})
            
    if request.user.is_active:
        leader_check = A2Study_access.objects.filter(
            leader=request.user, valid_till__gte=datetime.datetime.now())
        if len(leader_check) > 0:
            teacher_or_leader = Leader.objects.filter(Q(leader_roles="Teacher") | Q(leader_roles="Diary Leader"),
                                            leader_name=request.user, valid_till__gte=datetime.datetime.now(), )
            if len(teacher_or_leader) > 0:
                return render(request, "A2S-student-portal.html", {'role': teacher_or_leader[0].leader_roles,  'leader': request.user, 'expire_on': leader_check[0].valid_till})

        # Students work
        
    return render(request, "AVA-Error2.html", {'username': request.user, 'message': "Access to this portal has been blocked"})


@login_required(login_url=A2S_login)
def A2S_Study_Register(request):
    student = Student.objects.get(
        student_name__username__contains=request.POST['username'])
    entry = StudyRegister.objects.create(
        student=student.student_name, status="Studied", study_date=datetime.date.today(), study_time = datetime.datetime.now(),
        subject = request.POST['subject'], description = request.POST['desc'])
    entry.save()
    return render(request, "AVA-message-display.html", {'username': request.user, 'message': "Study time registered successfully"})


@login_required(login_url=A2S_login)
def A2S_Student_Home(request):
    student = Student.objects.filter(
        student_name=request.user, is_active=True, last_date__gte=datetime.datetime.now())
    sr = StudyRegister.objects.filter(student = request.user, study_date = datetime.datetime.now())
    
    if len(student) > 0:
        if len(sr) > 0:
            return render(request, "A2S-student-home.html", {'role': 'Student', 'student': request.user, 'is_reg': False, 
            'sr_time': sr[0].study_time, 'approved': sr[0].approved_by_trainer,
            'declined' : sr[0].declined_by_trainer, 'by' : sr[0].actioned_by
            })
        else:
            return render(request, "AVA-Error2.html", {'username': request.user, 'message': "Your account has been blocked"})

    else:
        return render(request, "AVA-Error2.html", {'username': request.user, 'message': "Access to this portal has been blocked"})


@login_required(login_url=A2S_login)
def A2S_Approved(request):
    leadername = request.POST['leadername']
    studentname = request.POST['studentname']
    sr = StudyRegister.objects.filter(
        student__username__contains=studentname, study_date=datetime.datetime.now()).update(approved_by_trainer=True, declined_by_trainer=False, actioned_by = leadername)
    
    return render(request, "AVA-message-display.html", {'username': request.user, 'message': "Study time has been approved by " + str(leadername)})


@login_required(login_url=A2S_login)
def A2S_Declined(request):
    leadername = request.POST['leadername']
    studentname = request.POST['studentname']
    sr = StudyRegister.objects.filter(
        student__username__contains=studentname, study_date=datetime.datetime.now()).update(approved_by_trainer=False, declined_by_trainer=True, actioned_by=leadername)

    return render(request, "AVA-message-display.html", {'username': request.user, 'message': "Study time has been rejected by " + str(leadername)})
