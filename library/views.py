from rest_framework.decorators import action
from rest_framework import viewsets
from .models import User, Book, Note
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from library.serializers import UserProfileSerializer, FeaturedBooksSerializer, NoteListInstanceSerializer, BookListInstanceSerializer, UserListInstanceSerializer


class FeaturedBooksViewSet(viewsets.ModelViewSet):
    '''
    filters Book model for attribute featured = True 
    '''
    serializer_class = FeaturedBooksSerializer

    def get_queryset(self):
        featured_books = Book.objects.filter(featured=True)
        return featured_books


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
