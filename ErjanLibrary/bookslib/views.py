from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Publisher, Author
from .forms import BookForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse


def book_list(request):
    books = Book.objects.all()
    return render(request, 'layout.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})  


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'

   

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})



class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'publisher', 'publication_date']
    success_url = reverse_lazy('book_list')
    template_name = 'book_update.html'

class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'

class AuthorCreateView(CreateView):
    model = Author
    fields = ['name']
    template_name = 'author_form.html'
    success_url = reverse_lazy('author_list.html')


class PublisherListView(ListView):
    model = Publisher
    template_name = 'publisher_list.html'

class PublisherCreateView(CreateView):
    model = Publisher
    fields = ['name']
    template_name = 'publisher_form.html'


def author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    return render(request, 'author_list.html', {'author': author})


