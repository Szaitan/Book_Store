from django.shortcuts import render, Http404, get_object_or_404
from .models import Book
from django.db.models import Avg


# Create your views here.


def index_page(request):
    all_books = Book.objects.all().order_by("-title")
    num_books = all_books.count()
    average_rating = all_books.aggregate(Avg("rating"))

    return render(request, "book_outlet/index.html", {
        "all_books": all_books,
        "total_number_books": num_books,
        "average_rating": average_rating,
    })


def detail_book_page(request, slug):
    # try:
    #     book = Book.objects.get(id=book_id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling,
    })
