from ast import Del, Mod
import http
from http.client import HTTPResponse
from multiprocessing import context
from re import search
from shutil import unregister_unpack_format
from telnetlib import SE
from urllib.parse import uses_fragment
from django.forms import PasswordInput
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import ListView, CreateView

from .forms import *
from .models import MyUser, Student, Track

# Create your views here.

def domainHomeView( request ): 
    return redirect( 'home/' )

def homeView( request ):

    context = {
        'insert_form' : Insert(),
        'update_form' : Update(), 
        'delete_form' : Delete(), 
        'search_form' : Search(), 
    }
    return render( request, 'amazon/home.html', context)


def aboutUsView( request ):
    return render( request, 'amazon/about-us.html')


def contactUsView( request ):
    return render( request, 'amazon/contact-us.html')

def msgSentView( request ):
    context = {}
    context[ 'user_email' ] = request.GET['uemail']
    context[ 'user_msg' ] = request.GET['msg']
    return render( request, 'amazon/msg-sent.html', context)


def loginView( request ):
    if request.method == 'POST':
        loginForm = Login(request.POST)
        
        if loginForm.is_valid():
            # extract entered username and password  
            username = loginForm.cleaned_data['user_name']
            password = loginForm.cleaned_data['password']

            user_name_exists = MyUser.objects.filter(user_name = username).exists()
            if not user_name_exists: 
                loginForm = Login()
                return render( request, 'amazon/login.html', {'form': loginForm, 'wrong_cred': 'username or password is incorrect'})

            password_correct = MyUser.objects.get( user_name = username).password == password 
            if not password_correct:
                loginForm = Login()
                return render( request, 'amazon/login.html', {'form': loginForm, 'wrong_cred': 'username or password is incorrect'})
            
            # everything is ok. let user log in and redirect it to home
            return redirect('/home/')
        else: 
            return HttpResponse('Something is wrong')
    else:
        loginForm = Login()
        return render( request, 'amazon/login.html', {'form': loginForm})


def registerView(request):
    if request.method == 'POST':
        regForm = Register( request.POST )
        if regForm.is_valid():
            # user_name exists ?
            # yes back to register with msg 
            # no store user in dp, redirect login 
            username = regForm.cleaned_data['user_name']
            password = regForm.cleaned_data['password']
            print( username, password)
            if MyUser.objects.filter( user_name = username ).exists(): 
                regForm = Register()
                return render(request, 'amazon/register.html', {'form': regForm, 'wrong_cred': 'username is taken'})
            
            # register user in db and redirect to login 
            MyUser.objects.create( user_name = username, password = password )
            return render( request, 'amazon/login.html', {'form': Login()} )
                 
    else: 
        registerForm = Register()
        return render( request, 'amazon/register.html', {'form': registerForm})




# student management views 
def insertStudent( req ):
    if req.method == 'POST':
        insertForm = Insert( req.POST )
        # duplicate student names is allowed. name is not pk. 
        if insertForm.is_valid():
                Student.objects.create( name=insertForm.cleaned_data['name'], age=insertForm.cleaned_data['age'], notes=insertForm.cleaned_data['notes']);
                return render( req, 'amazon/status.html', {'status': 'success'})

    return redirect('/home/')

def updateStudent( req ):
    if req.method == 'POST':
        updateForm = Update( req.POST )
        # duplicate student names is allowed. name is not pk. 
        if updateForm.is_valid():
            nname, nage, nnotes= updateForm.cleaned_data['new_name'], updateForm.cleaned_data['new_age'], updateForm.cleaned_data['new_notes']
            Student.objects.filter(name = updateForm.cleaned_data['name']).update(name=nname, age=nage, notes=nnotes)
            return render( req, 'amazon/status.html', {'status': 'success'})
    return redirect('/home/')



def deleteStudent( req ):
    if req.method == 'POST':
        sform = Delete( req.POST )
        # duplicate student names is allowed. name is not pk. 
        if sform.is_valid():
                Student.objects.filter( name=sform.cleaned_data['name']).delete()
                return render( req, 'amazon/status.html', {'status': 'successful'})
    return redirect('/home/')

def showAllStudent( req ):
    return render( req, 'amazon/search-results.html', { 'students': Student.objects.all()}) 

def searchStudent( req ):
    if req.method == 'POST':
        sform = Search( req.POST )
        # duplicate student names is allowed. name is not pk. 
        if sform.is_valid():
                studentList = Student.objects.filter( name=sform.cleaned_data['name'])
                return render( req, 'amazon/search-results.html', {'students': studentList})
    return redirect('/home/') 



