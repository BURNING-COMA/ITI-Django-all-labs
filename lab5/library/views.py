from django.shortcuts import redirect, render
from library.models import Author, Book

from .forms import AddBookForm

# Create your views here.
def autherInfoView( request, author_id ):
    authorData = Author.objects.get( id=author_id)
    authorBooks = Book.objects.filter( author_id = authorData.id)
    context = { 
        'authorData' : authorData,
        'books' : authorBooks,
    }
    return render(request, "library/author-info.html", context)

def showAllAuthors( request ):
    authors = Author.objects.all()
    context = {
        'authors' : authors,
    }
    return render( request, "library/all-authors.html", context )

def insertAuthorForm( request ):
    return render(request, 'library/insert-author.html')

def insertAuthor( request ):
    newAuthorFirstName = request.GET['first_name']
    newAuthorLastName = request.GET['last_name']
    Author.objects.create(first_name = newAuthorFirstName, last_name = newAuthorLastName )
    return redirect('insert-author-form')



def index(request):
    form = AddBookForm()
    return render( request, 'library/index.html', {'form' : form})