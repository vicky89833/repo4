from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from testapp.models import Book

class BookListView(ListView):
    model=Book
    #default template file: book_list.html
    # template_name = 'testapp/books.html'
    #default context object name: book_list
    # context_object_name = 'books'

class BookListView2(ListView):
    model=Book
    template_name='testapp/books.html'
    context_object_name= 'books'

class BookDetailView(DetailView):
    model = Book
    #default template file: book_detail.html
    #default context object:book or object

class BookCreateView(CreateView):
    model = Book
    #fields = ('title','author','pages','price')
    fields = '__all__'
class BookUpdateView(UpdateView):
    model = Book
    fields='__all__'
    #The default template is: book_form.html

from django.urls import reverse_lazy
class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('listbooks')
