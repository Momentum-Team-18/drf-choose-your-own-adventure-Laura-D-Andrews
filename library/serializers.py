from .models import User, Book, Note, Status
from rest_framework import serializers


class NoteListInstanceSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Basic serializer for Note model
    Filters for public notes
    Links to note list and note instance
    Can filter by book_title
    NoteViewSet

    '''
    class Meta:
        model = Note
        fields = ['url', 'note_title', 'note_text',
                  'book', 'commenter', 'privacy']
# additional goal - filter for user's notes (private and public)


class UserListInstanceSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Basic list serializer for User model
    Admin access only

    '''

    class Meta:
        model = User
        exclude = ['password']


class UserProfileSerializer(serializers.ModelSerializer):
    '''
    User profile list
    UserProfileViewSet
    '''
    notes_by_commenter = NoteListInstanceSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'notes_by_commenter']


class BookListInstanceSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Basic serializer for Book model
    Links to book list and book instance
    Can filter for author or book_title
    BookViewSet
    '''

    class Meta:
        model = Book
        fields = ['url', 'book_title', 'author',
                  'year', 'featured', 'notes_about_book']
# additional goal - can see all user public comments in note detail


class FeaturedBooksSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Serializer to display 'featured' books list filtered for featured=True
    Can also filter for author or book_title
    BookFeaturedViewSet
    '''
    class Meta:
        model = Book
        fields = ['url', 'book_title', 'author', 'featured']
# additional goal - can see all user public comments in note detail


class UserReadSerializer(serializers.HyperlinkedModelSerializer):
    '''
    User-specific serializer for books user has read
    UserReadViewSet
    '''
    class Meta:
        model = Status
        fields = ['read', 'user', 'book']


class UserReadingSerializer(serializers.HyperlinkedModelSerializer):
    '''
    User-specific serializer for books user is reading
    UserReadingViewSet
    '''
    class Meta:
        model = Status
        fields = ['reading', 'user', 'book']


class UserWantToReadSerializer(serializers.HyperlinkedModelSerializer):
    '''
    User-specifiv serializer for books user wants to read
    UserWantToReadViewSet
    '''
    class Meta:
        model = Status
        fields = ['want_to_read', 'user', 'book']
