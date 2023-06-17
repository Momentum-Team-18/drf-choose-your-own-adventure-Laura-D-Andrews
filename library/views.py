from rest_framework.decorators import action
from rest_framework import viewsets
from .models import User, Book, Note, Status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from library.serializers import UserWantToReadSerializer, UserReadingSerializer, UserReadSerializer, UserProfileSerializer, FeaturedBooksSerializer, NoteListInstanceSerializer, BookListInstanceSerializer, UserListInstanceSerializer


class FeaturedBooksViewSet(viewsets.ModelViewSet):
    '''
    filters Book model for attribute featured = True 
    '''
    serializer_class = FeaturedBooksSerializer

    def get_queryset(self):
        featured_books = Book.objects.filter(featured=True)
        return featured_books


class UserReadViewSet(viewsets.ModelViewSet):
    '''
    filters Status model for attribute read=True
    '''
    serializer_class = UserReadSerializer

    def get_queryset(self):
        books_read = Status.objects.filter(read=True)
        return books_read
# how to filter for just signed in user


class UserReadingViewSet(viewsets.ModelViewSet):
    '''
    filters Status model for attribute reading=True
    '''
    serializer_class = UserReadingSerializer

    def get_queryset(self):
        books_reading = Status.objects.filter(reading=True)
        return books_reading


class UserWantToReadViewSet(viewsets.ModelViewSet):
    '''
    filters Status model for attribute want_to_read=True
    '''
    serializer_class = UserWantToReadSerializer

    def get_queryset(self):
        want_to_read_books = Status.objects.filter(want_to_read=True)
        return want_to_read_books


class NoteViewSet(viewsets.ModelViewSet):
    '''
    receives and returns request for all Note objects
    '''
    queryset = Note.objects.all()
    serializer_class = NoteListInstanceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookViewSet(viewsets.ModelViewSet):
    '''
    receives and returns request for all Book objects
    '''
    queryset = Book.objects.all()
    serializer_class = BookListInstanceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    receives and returns request for hopefully only username
    '''
    queryset = User.objects.all()
    serializer_class = UserListInstanceSerializer
    # permission_classes = [IsAuthenticated]


class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    receives and returns request for all User objects
    '''
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    # add permission so only user can see
