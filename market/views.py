
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, Page

from .models import Book


def get_books(request):
    books = Book.objects.all()
    paginator = Paginator(books, per_page = 2)
    page_num = int(request.GET.get('page', 1))
    page : Page = paginator.get_page(page_num)
    return render(request, 'index.html', {'books': page})



def get_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'detail.html', {'books': [book]})


