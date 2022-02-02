from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homeView( request ):
    page_content = '''
    <center> 
    <!-- nav bar -->
    <div>
        <a href="http://localhost:8000/home">Home</a> <pre>   </pre>
        <a href="http://localhost:8000/contact-us">Contact Us</a> <pre>   </pre>
        <a href="http://localhost:8000/about-us">About Us</a> <pre>   </pre>
    </div>

    <h1>Welcome</h1>
    <p> both  http://localhost:8000/home/ and http://localhost:8000/ <br> lead to homeView view <br> which respond with this page
    </p>
    </center>
    '''

    return HttpResponse(page_content)


def aboutUsView( request ):
    return render( request, 'amazon/about-us.html')


def contactUsView( request ):
    return render( request, 'amazon/contact-us.html')

def msgSentView( request ):
    context = {}
    context[ 'user_email' ] = request.GET['uemail']
    context[ 'user_msg' ] = request.GET['msg']
    return render( request, 'amazon/msg-sent.html', context)