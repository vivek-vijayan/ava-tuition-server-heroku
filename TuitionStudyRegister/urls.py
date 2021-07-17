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
from .views import A2S_Home, A2S_logout, A2S_Student_Home, A2S_Study_Register, A2S_Detail, A2S_Approved, A2S_Declined


urlpatterns = [
    path('home', A2S_Home, name="A2S_Home"),
    path('logout', A2S_logout, name="A2S_logout"),
    path('stud-home', A2S_Student_Home, name="A2S_Student_Home"),
    path('register', A2S_Study_Register, name="A2S_Study_Register"),
    path('show-detail', A2S_Detail, name="A2S_Detail"),
    path('approved', A2S_Approved, name="A2S_Approved"),
    path('declined', A2S_Declined, name="A2S_Declined"),
    
]
