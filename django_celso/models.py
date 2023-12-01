from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    name = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name
    class Meta: 
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Books(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    picture = models.ImageField(blank=False)
    cod = models.IntegerField(unique=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    qtd = models.IntegerField()
    discount = models.IntegerField()
    created_at = models.DateField()
    in_stock = models.BooleanField(default=False)
    # emprestado = models.BooleanField(default=False)
    # usuario_que_pegou = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    # data_devolucao = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class Loan(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_borrowed = models.DateTimeField(auto_now_add=True)
    return_due_date = models.DateTimeField()
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
    


    