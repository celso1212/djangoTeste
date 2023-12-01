from django.shortcuts import render

from django.shortcuts import render, HttpResponse, redirect
from .models import Books, Categories
from random import randint
from datetime import datetime
from .models import Loan
from .forms import LoanForm
from .forms import BorrowBookForm


def index(request):
    books = Books.objects.all()
    for book in books:
        print(book.name)
    return render(request, 'pages/index.html', {'books':books})

def all_books(request):
    books = Books.objects.all()
    return render(request, 'all_books.html', {'books': books})

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

def sell_book(request, id):
    book = Books.objects.get(id=id)
    book.qtd -= 1
    if book.qtd == 0:
        book.in_stock = False
    book.save()
    return redirect('book_details', id)

def borrow_book(request, id):
    if request.method == 'POST':
        form = BorrowBookForm(request.POST)
        if form.is_valid():
            action = request.POST.get('action')
            if action == 'borrow':
                # Lógica para pegar o livro
                # Adicione aqui o que for necessário para processar o empréstimo
                return redirect('sucesso_emprestimo')  # Redireciona para uma página de sucesso
            elif action == 'return':
                # Lógica para devolver o livro
                # Adicione aqui o que for necessário para processar a devolução
                return redirect('sucesso_devolucao')  # Redireciona para uma página de sucesso
    else:
        form = BorrowBookForm()

    return render(request, 'borrow_book.html', {'form': form})
