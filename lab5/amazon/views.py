# TODO 

from ast import Del, Mod
import http
from http.client import HTTPResponse
from multiprocessing import context
from re import search
from shutil import unregister_unpack_format
from telnetlib import SE
from urllib import request
from urllib.parse import uses_fragment
from django.forms import PasswordInput
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, CreateView

from django.views.decorators.http import require_http_methods

from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from rest_framework import permissions
from amazon.serializers import UserSerializer, GroupSerializer, StudentSerializer, TrackSerializer, IntakeSerializer

from .forms import *
from .models import MyUser, Student, Track, Intake

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def domainHomeView( request ): 
    if not request.user.is_authenticated:
        return redirect('/login/')
  
    return redirect('/home/')

def homeView( request ):
    # verify user is logged in
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')

    context = {
        'insert_form' : Insert(),
        'update_form' : Update(), 
        'delete_form' : Delete(), 
        'search_form' : Search(), 
    }
    return render( request, 'amazon/home.html', context)
  
        


def aboutUsView( request ):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render( request, 'amazon/about-us.html')


def contactUsView( request ):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render( request, 'amazon/contact-us.html')

def msgSentView( request ):
    if not request.user.is_authenticated:
        return redirect('/login/')
    context = {}
    context[ 'user_email' ] = request.GET['uemail']
    context[ 'user_msg' ] = request.GET['msg']
    return render( request, 'amazon/msg-sent.html', context)


def loginView( request ):
    # if user is logged in, send it home
    if request.user.is_authenticated:
        return redirect('/home/')
    
    if request.method == 'POST':
        loginForm = Login(request.POST) 
        if loginForm.is_valid():
            # extract entered username and password  
            username = loginForm.cleaned_data['user_name']
            password = loginForm.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None: 
                request.session['username'] = username
                login( request, user)
                return redirect( '/home/')
            else: 
                loginForm = Login()
                return render( request, 'amazon/login.html', {'form': loginForm, 'msg': 'username or password is incorrect'})
        else: 
            return HttpResponse('Something is wrong')
    else:
        loginForm = Login()
        return render( request, 'amazon/login.html', {'form': loginForm})


def registerView(request):
    if request.user.is_authenticated:
            return redirect('/home/')
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
                return render(request, 'amazon/register.html', {'form': regForm, 'msg': 'username is taken'})
            
            # register user in db and redirect to login 
            MyUser.objects.create( user_name = username, password = password )
            # add user to User admin model
            User.objects.create_user( username = username, password = password, is_staff = True  )
            return render( request, 'amazon/login.html', {'form': Login(), 'msg' : 'Registered! Please log in'} )
                 
    else: 
        registerForm = Register()
        return render( request, 'amazon/register.html', {'form': registerForm})






# student management views
@require_http_methods(['POST']) 
def insertStudent( req ):
    if not req.user.is_authenticated:
            return redirect('/login/')
    insertForm = Insert( req.POST )
    # duplicate student names is allowed. name is not pk. 
    if insertForm.is_valid():
            insertForm.save()
            return render( req, 'amazon/status.html', {'status': 'success'})

# def updateStudent( req ):
#     if not req.user.is_authenticated:
#         return redirect('/login/')

#     if req.method == 'POST':
#         updateForm = Update( req.POST )
#         # duplicate student names is allowed. name is not pk. 
#         if updateForm.is_valid():
#             nname, nage, nnotes= updateForm.cleaned_data['new_name'], updateForm.cleaned_data['new_age'], updateForm.cleaned_data['new_notes']
#             Student.objects.filter(name = updateForm.cleaned_data['name']).update(name=nname, age=nage, notes=nnotes)
#             return render( req, 'amazon/status.html', {'status': 'success'})
#     return redirect('/home/')



# class-based view for updateStudent    
class updateStudent( View ):
     #method to be called if request Method is GET
    def get(self, req):
        if not req.user.is_authenticated:
            return redirect('/login/')
        return redirect('/home/')
    #Method to be called if request Method is GET
    def post(self, req):
        # is it possible to recieve a POST request from unlogged in user ? 
        # regardless, just block it
        if not req.user.is_authenticated:
            return redirect('/login/')

        targetStudent = Student.objects.get( id = req.POST['student_id'])
        # update( req.POST ) will lead to creation of new Student
        # Instead, we must use modelformname( req.POST, instance=targetObject)
        # https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/
        updateStudentForm = Update( req.POST, instance=targetStudent )

        # .is_valid() call is not necessary since .save() will do checks automatically ?
        # if updateStudentForm.is_valid():

        # nname, nage, nnotes= updateForm.cleaned_data['name'], updateForm.cleaned_data['age'], updateForm.cleaned_data['notes']
        # Student.objects.filter(id = updateForm.cleaned_data['student_id']).update(name=nname, age=nage, notes=nnotes)

        updateStudentForm.save()
        return render( req, 'amazon/status.html', {'status': 'success'})
        



def deleteStudent( req ):
    if not req.user.is_authenticated:
        return redirect('/login/')
    if req.method == 'POST':
        sform = Delete( req.POST )
        # duplicate student names is allowed. name is not pk. 
        if sform.is_valid():
                Student.objects.filter( id=sform.cleaned_data['student_id']).delete()
                return render( req, 'amazon/status.html', {'status': 'successful'})
    return redirect('/home/')




def showAllStudent( req ):
    if not req.user.is_authenticated:
        return redirect('/login/')
    return render( req, 'amazon/search-results.html', { 'students': Student.objects.all()}) 



def searchStudent( req ):
    if not req.user.is_authenticated:
        return redirect('/login/')
    if req.method == 'POST':
        sform = Search( req.POST )
        # duplicate student names is allowed. name is not pk. 
        if sform.is_valid():
                studentList = Student.objects.filter( name=sform.cleaned_data['name'])
                return render( req, 'amazon/search-results.html', {'students': studentList})
    return redirect('/home/') 



def logoutView( req ):
    if not req.user.is_authenticated:
        return redirect('/login/')
    logout(req)
    req.session.clear()
    return redirect('/login/')




# generic class-based views 

@method_decorator(login_required, name='dispatch')
class CreateTrack( CreateView ) :
    fields = '__all__'
    model = Track
    def get_success_url(self):
        # redirect('listTrack/')# for some reason, it appends /listTrack to CreatTrack causing error
        return reverse('listTrack')



@method_decorator(login_required, name='dispatch')
class ListTrack( ListView ):
    model = Track


# api views 
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows students to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer 
    permission_classes = [permissions.IsAuthenticated]


class TrackViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tracks to be viewed or edited.
    """
    queryset = Track.objects.all()
    serializer_class = TrackSerializer 
    permission_classes = [permissions.IsAuthenticated]


class IntakeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows intakes to be views or edited. 
    """
    queryset = Intake.objects.all()
    serializer_class = IntakeSerializer
    permission_classes = [permissions.IsAuthenticated]



@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})



from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
  
from .models import Student
from .serializers import StudentSerializer
  

  
@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=404)
  
    if request.method == 'GET':
        serializer = StudentSerializer(student, context={'request': request})
        return Response(serializer.data)
  
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(student, context={'request': request})
  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=204)
