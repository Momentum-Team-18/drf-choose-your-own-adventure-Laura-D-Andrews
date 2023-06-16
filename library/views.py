from rest_framework.decorators import action
from rest_framework import permissions, renderers, viewsets, generics
from .models import User, Book, Note
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, SAFE_METHODS
from library.serializers import NoteListInstanceSerializer, BookListInstanceSerializer, UserListInstanceSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteListInstanceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookListInstanceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListInstanceSerializer
    permission_classes = [IsAuthenticated]
