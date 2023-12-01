from django import forms
from .models import Loan  
from django import forms
from .models import Books


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['book', 'return_due_date']


class BorrowBookForm(forms.Form):
    books = Books.objects.all()
    book_choices = [(book.name, book.name) for book in books]

    book = forms.ChoiceField(choices=book_choices, label="Livro")
    borrower_name = forms.CharField(max_length=100, label="Seu Nome")
    borrow_date = forms.DateField(
        label="Data de Empréstimo",
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'],
    )