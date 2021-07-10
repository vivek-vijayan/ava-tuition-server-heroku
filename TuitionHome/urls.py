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
from .views import AVA_login, AVA_logginer, AVA_Home, AVA_logout

urlpatterns = [
    path('', AVA_login, name="AVA_login"),
    path('login', AVA_logginer, name="AVA_logginer"),
    path('logout', AVA_logout, name="AVA_Logout"),
    path('home', AVA_Home, name="AVA_logginer"),
]
