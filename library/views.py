from rest_framework.decorators import action
from rest_framework import viewsets
from .models import User, Book, Note
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from library.serializers import FeaturedBooksSerializer, NoteListInstanceSerializer, BookListInstanceSerializer, UserListInstanceSerializer


class FeaturedBooksViewSet(viewsets.ModelViewSet):
    serializer_class = FeaturedBooksSerializer

    def get_queryset(self):
        featured_books = Book.objects.filter(featured=True)
        return featured_books


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


# class FeaturedBooksViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = FeaturedBooksSerializer
#     filter_set_fields = ['featured']
