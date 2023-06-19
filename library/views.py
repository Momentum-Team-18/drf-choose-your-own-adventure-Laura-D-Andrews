from rest_framework.decorators import action
from rest_framework import viewsets
from .models import User, Book, Note, Status
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from library.serializers import UserReadSerializer, UserReadingSerializer, UserWantToReadSerializer, UserProfileSerializer, FeaturedBooksSerializer, NoteListInstanceSerializer, BookListInstanceSerializer, UserListInstanceSerializer


'''
user viewsets
'''


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    receives and returns request for list of users (only username specified in serializer)
    '''
    queryset = User.objects.all()
    serializer_class = UserListInstanceSerializer
    permission_classes = [IsAuthenticated]


class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    receives and returns request for all User attribute fields in specified in serializer
    '''
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer


class UserReadViewSet(viewsets.ModelViewSet):
    '''
    filters Status model for signed in user and for attribute read=True
    '''
    serializer_class = UserReadSerializer

    def get_queryset(self):
        return self.request.user.user_relation_to_status.filter(read=True)


class UserReadingViewSet(viewsets.ModelViewSet):
    '''
    filters Status model for signed in user and for attribute reading=True
    '''
    serializer_class = UserReadingSerializer

    def get_queryset(self):
        return self.request.user.user_relation_to_status.filter(reading=True)


class UserWantToReadViewSet(viewsets.ModelViewSet):
    '''
    filters Status model for signed in user attribute want_to_read=True
    '''
    serializer_class = UserWantToReadSerializer

    def get_queryset(self):
        return self.request.user.user_relation_to_status.filter(want_to_read=True)


'''
book view sets
'''


class BookViewSet(viewsets.ModelViewSet):
    '''
    receives and returns request for all Book objects, option to search/filter by book author or title
    '''
    filter_backends = (filters.SearchFilter,)
    search_fields = ['author', 'book_title']
    queryset = Book.objects.all()
    serializer_class = BookListInstanceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# on render author and title filter working


class FeaturedBooksViewSet(viewsets.ModelViewSet):
    '''
    filters Book model for attribute featured = True , optional search/filter for book title or author
    '''
    filter_backends = (filters.SearchFilter,)
    search_fields = ['author', 'book_title']
    serializer_class = FeaturedBooksSerializer

    def get_queryset(self):
        featured_books = Book.objects.filter(featured=True)
        return featured_books


'''
note viewsets
'''


class NoteViewSet(viewsets.ModelViewSet):
    '''
    receives and returns request for all Note objects, option to search/filter for book title
    '''
    filter_backends = (filters.SearchFilter,)
    search_fields = ['book__book_title']
    queryset = Note.objects.all()
    serializer_class = NoteListInstanceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
