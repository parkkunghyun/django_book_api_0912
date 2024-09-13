from rest_framework import viewsets, filters
from .models import Book, Category, Author
from .serializers import AuthorSerializer, CategorySerializer, BookSerializer
from django_filters.rest_framework import DjangoFilterBackend

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['author', 'categories']
    search_fields = ['title', 'author__name']
