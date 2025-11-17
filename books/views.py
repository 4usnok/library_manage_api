from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from books.models import Books
from books.serializers import BooksSerializer

class BooksList(generics.ListAPIView):
    """Просмотр списка книг"""
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

class BooksCreate(generics.ListCreateAPIView):
    """Создание книги"""
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

class BooksDestroy(generics.DestroyAPIView):
    """Удаление книги"""
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class BooksUpdate(generics.UpdateAPIView):
    """Редактирование книги"""
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class BooksRetrieve(generics.RetrieveAPIView):
    """Просмотр одной книги"""
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
