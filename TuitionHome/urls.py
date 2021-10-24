"""TuitionServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from .views import AVA_login, AVA_logginer, AVA_Home, AVA_logout, AVA_A2P_self_absent_apply, AVA_A2P_self_absent_request, show_leader, AVA_password_reset, AVA_change_password, AVA_Exam_Result



urlpatterns = [
    path('', AVA_login, name="AVA_login"),
    path('exam-score', AVA_Exam_Result, name="AVA_Exam_Result"),
    path('login', AVA_logginer, name="AVA_logginer"),
    path('logout', AVA_logout, name="AVA_Logout"),
    path('self-absent-raise', AVA_A2P_self_absent_request, name="self-absent-raise"),
    path('self-absent-apply', AVA_A2P_self_absent_apply, name="self-absent-apply"),
    path('home', AVA_Home, name="AVA_logginer"),
    path('show/<user_id>', show_leader, name="show"),
    path('password-change', AVA_password_reset, name="AVA_password_reset"),
    path('password-resetting', AVA_change_password, name="AVA_change_password"),
]
