from rest_framework.decorators import action
from rest_framework import permissions, renderers, viewsets
from rest_framework.response import Response
from .models import User, Book, Note
from library.permissions import IsOwnerOrReadOnly
from library.serializers import UserSerializer, BookSerializer, NoteSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_class = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]


# save????
