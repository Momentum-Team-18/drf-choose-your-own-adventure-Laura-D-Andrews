from rest_framework.decorators import action
from rest_framework import viewsets
from .models import User, Book, Note, Status
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from library.serializers import UserReadSerializer, UserReadingSerializer, UserWantToReadSerializer, UserProfileSerializer, FeaturedBooksSerializer, NoteListInstanceSerializer, BookListInstanceSerializer, UserListInstanceSerializer


class SearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


'''
user viewsets
'''


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    receives and returns request for list of only users
    '''
    queryset = User.objects.all()
    serializer_class = UserListInstanceSerializer
    # permission_classes = [IsAuthenticated]


class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    receives and returns request for all User attributes
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
    receives and returns request for all Book objects, option to search/filter by author or title
    '''

    filter_backends = (SearchFilter,)
    search_fields = ['author', 'book_title']
    filter_backends = (filters.SearchFilter,)
    queryset = Book.objects.all()
    serializer_class = BookListInstanceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class FeaturedBooksViewSet(viewsets.ModelViewSet):
    '''
    filters Book model for attribute featured = True 
    '''
    serializer_class = FeaturedBooksSerializer

    def get_queryset(self):
        featured_books = Book.objects.filter(featured=True)
        return featured_books


'''
note viewsets
'''


class NoteViewSet(viewsets.ModelViewSet):
    '''
    receives and returns request for all Note objects
    '''
    search_fields = ['book__book_title']
    filter_backends = (filters.SearchFilter,)
    queryset = Note.objects.all()
    serializer_class = NoteListInstanceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
