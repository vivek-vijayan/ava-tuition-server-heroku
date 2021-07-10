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
from .views import A2P_display, A2P_query, A2P_checkin, A2P_checkout, A2P_login, A2P_logginer, A2P_complain_register, A2P_logout

urlpatterns = [
    path('a2portal', A2P_display, name="Attendance Homepage"),
    path('query', A2P_query, name="Attendance query"),
    path('checkin', A2P_checkin, name="checkin query"),
    path('checkout', A2P_checkout, name="checkout query"),
    path('login', A2P_login, name="A2P_login"),
    path('logout', A2P_logout, name="A2P_logout"),
    path('loginer', A2P_logginer, name="A2P_logginer"),
    path('complain', A2P_complain_register, name="A2P_complain_register")

]
