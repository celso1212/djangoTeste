from django.shortcuts import render

from django.shortcuts import render, HttpResponse, redirect
from .models import Books, Categories
from random import randint
from datetime import datetime
def index(request):
    books = Books.objects.all()
    for book in books:
        print(book.name)
    return render(request, 'pages/index.html', {'books':books})

def add_book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        cod = randint(100, 10000)
        category = request.POST.get('category')
        picture = request.FILES.get('picture')
        price = request.POST.get('price')
        description = request.POST.get('description')
        qtd = request.POST.get('qtd')
        discount = request.POST.get('discount')
        created_at = datetime.now()
        in_stock = True

    
        Books.objects.create(
            name=name,cod=cod,category_id=category,
            picture=picture, price=price, description=description,
            qtd=qtd,discount=discount,created_at=created_at,in_stock=in_stock
        )
        return redirect('home')
    else:
        categories = Categories.objects.all()
        return render(request, 'pages/add-book.html', {'categories':categories})


def book_details(request, id):
    book = Books.objects.get(id=id)
    return render(request, 'pages/book_details.html', {'book':book})

def delete_book(request, id):
    book = Books.objects.get(id=id)
    book.delete()
    return redirect('home')
