from .models import User, Book, Note, Status
from rest_framework import serializers

# LIST OUT GET?POST ETC


class NoteListInstanceSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Basic serializer for Note model
    Filters for public notes
    Links to note list and note instance
    '''
    class Meta:
        model = Note
        fields = ['url', 'note_title', 'note_text',
                  'book', 'commenter', 'privacy']


class UserListInstanceSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Basic list serializer for User model
    Admin access only
    '''

    class Meta:
        model = User
        exclude = ['password']


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    '''
    User profile serializer
    '''
    class Meta:
        model = User
        fields = ['username']


class BookListInstanceSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Basic serializer for Book model
    Links to book list and book instance
    '''

    class Meta:
        model = Book
        fields = ['url', 'book_title', 'author',
                  'year', 'featured']


class FeaturedBooksSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Serializer to display 'featured' books list filtered for featured=True
    '''
    class Meta:
        model = Book
        fields = ['url', 'book_title', 'author', 'featured']


class UserReadSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Serializer for books user has read
    '''
    class Meta:
        model = Status
        fields = ['read', 'user', 'book']


class UserReadingSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Serializer for books user is reading
    '''
    class Meta:
        model = Status
        fields = ['reading', 'user', 'book']


class UserWantToReadSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Serializer for books user wants to read
    '''
    class Meta:
        model = Status
        fields = ['want_to_read', 'user', 'book']
