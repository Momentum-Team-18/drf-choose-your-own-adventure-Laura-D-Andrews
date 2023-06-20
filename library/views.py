from rest_framework import viewsets
from .models import User, Book, Note, Status
from rest_framework import filters
from rest_framework import permissions
from library.serializers import UserReadSerializer, UserReadingSerializer, UserWantToReadSerializer, UserProfileSerializer, FeaturedBooksSerializer, NoteListInstanceSerializer, BookListInstanceSerializer, UserListInstanceSerializer


'''
user viewsets
'''


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    Receives and returns request for list of users and user details
    Only admin access
    '''
    queryset = User.objects.all()
    serializer_class = UserListInstanceSerializer
    permission_classes = [permissions.IsAdminUser]


class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    Receives and returns request for all User attribute fields specified in serializer
    Includes user private notes
    '''
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class UserReadViewSet(viewsets.ModelViewSet):
    '''
    Filters Status model for signed in user and for attribute read=True
    '''
    serializer_class = UserReadSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.request.user.user_relation_to_status.filter(read=True)


class UserReadingViewSet(viewsets.ModelViewSet):
    '''
    Filters Status model for signed in user and for attribute reading=True
    '''
    serializer_class = UserReadingSerializer

    def get_queryset(self):
        return self.request.user.user_relation_to_status.filter(reading=True)


class UserWantToReadViewSet(viewsets.ModelViewSet):
    '''
    Filters Status model for signed in user attribute want_to_read=True
    '''
    serializer_class = UserWantToReadSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.request.user.user_relation_to_status.filter(want_to_read=True)


'''
book view sets
'''


class BookViewSet(viewsets.ModelViewSet):
    '''
    Receives and returns request for all Book objects
    Option to search/filter by book author or title
    '''
    serializer_class = BookListInstanceSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['author', 'book_title']
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FeaturedBooksViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    Filters Book model for attribute featured = True
    Option search/filter for book title or author
    '''
    serializer_class = FeaturedBooksSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['author', 'book_title']

    def get_queryset(self):
        featured_books = Book.objects.filter(featured=True)
        return featured_books


'''
note viewsets
'''


class NoteViewSet(viewsets.ModelViewSet):
    '''
    Receives and returns request for Note model
    Option to search/filter for book title
    '''
    serializer_class = NoteListInstanceSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['book__book_title']
    queryset = Note.objects.all()

    def get_queryset(self):
        return Note.objects.filter(privacy=False)
