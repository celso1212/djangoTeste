from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('add-books/', views.add_book, name='add_book'),
    path('delete-book/<int:id>/', views.delete_book, name='delete_book'),
    path('book-details/<int:id>/', views.book_details, name='book-details')
]