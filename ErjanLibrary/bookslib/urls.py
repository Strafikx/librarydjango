from django.urls import path
from bookslib.views import book_list, book_detail, book_create
from .views import BookCreateView, BookUpdateView, AuthorListView, AuthorCreateView, PublisherListView, PublisherCreateView
from . import views


urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('books/<int:pk>/', book_detail, name='book_detail'),
    path('book/create/', BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('author/<int:pk>/', views.author_detail, name='author_detail'),
    path('author/create/', AuthorCreateView.as_view(), name='author_create'),
    path('publisher/', PublisherListView.as_view(), name='publisher_list'),
    path('publisher/create/', PublisherCreateView.as_view(), name='publisher_create'),
]