from django.urls import path
from . import views
from .views import borrow_book


urlpatterns = [
    path('', views.index, name='home'),
    path('add-books/', views.add_book, name='add_book'),
    path('delete-book/<int:id>/', views.delete_book, name='delete_book'),
    path('all_books/', views.all_books, name='all_books'),
    path('sell-book/<int:id>/', views.sell_book, name='sell-book'),
    path('book-details/<int:id>/', views.book_details, name='book-details'),
    path('borrow/<int:id>/', views.borrow_book, name='borrow_book'),
    path('book-details/<int:pk>/', views.book_details, name='book_details')


]