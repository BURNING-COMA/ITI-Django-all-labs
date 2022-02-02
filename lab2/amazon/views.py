from http.client import HTTPResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.

def domainHomeView( request ): 
    return redirect( 'home/' )

def homeView( request ):
    return render( request, 'amazon/home.html')


def aboutUsView( request ):
    return render( request, 'amazon/about-us.html')


def contactUsView( request ):
    return render( request, 'amazon/contact-us.html')

def msgSentView( request ):
    context = {}
    context[ 'user_email' ] = request.GET['uemail']
    context[ 'user_msg' ] = request.GET['msg']
    return render( request, 'amazon/msg-sent.html', context)