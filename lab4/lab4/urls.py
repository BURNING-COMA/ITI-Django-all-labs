"""lab4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from amazon.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homeView, name='home'),
    path('', domainHomeView, name='login'),
    path('about-us/', aboutUsView, name='aboutUs'), 
    path('contact-us/', contactUsView,name='contactUs'),
    path('msg-sent/', msgSentView, name='msgSent'),
    path('login/', loginView, name='login'),
    path('register/', registerView, name='register'),
    path('logout/', logoutView, name='logout'),

    path('insert', insertStudent, name='insert'),
    path('update', updateStudent, name='update'),
    path('delete', deleteStudent, name='delete'),
    path('search', searchStudent, name='search'),
    path('selectAll', showAllStudent, name='selectAll'),

    path('cars/', include('cars.urls')),
    path('library/', include('library.urls'))
]
