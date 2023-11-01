from django.shortcuts import render
from .models import Book

# Create your views here.


def index_page(request):
    all_books = Book.objects.all()
    return render(request, "book_outlet/index.html", {
        "all_books": all_books
    })

