from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from authors.models import Authors
from authors.serializers import AuthorsSerializer

class AuthorsList(generics.ListAPIView):
    """Просмотр списка авторов"""
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer

class AuthorsCreate(generics.ListCreateAPIView):
    """Создание автора"""
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer

class AuthorsDestroy(generics.DestroyAPIView):
    """Удаление автора"""
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class AuthorsUpdate(generics.UpdateAPIView):
    """Редактирование автора"""
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class AuthorsRetrieve(generics.RetrieveAPIView):
    """Просмотр подробной информации об авторе"""
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer
