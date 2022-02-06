from django.urls import path

from . import views



urlpatterns = [

    path("<int:author_id>/", views.autherInfoView, name="authorInfoView"),
    path("all-authors", views.showAllAuthors, name="showAllAuthors"),
    path("insert-author", views.insertAuthor, name='insert-author'),
    path("insert-author-form", views.insertAuthorForm, name='insert-author-form'),
    path('index', views.index, name='index')

]