from django.urls import path
from . import views

urlpatterns = [
    path('books/uploadfile', views.uploadfile, name='uploadfile'),
    path('books/bookdashboard', views.bookdashboard, name='bookdashboard'),
    path('books/delete-book/<int:id>/', views.deleteBook, name='deleteBook'),
]