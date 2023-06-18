from .models import User, Book, Note, Status
from rest_framework import serializers


class NoteListInstanceSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Basic serializer for Note model, objects.all queryset, links to note list and note instance
    '''
    class Meta:
        model = Note
        fields = ['url', 'note_title', 'public_note_text', 'book', 'user']


class BookListInstanceSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Basic serializer for Book model, objects.all queryset, links to book list and book instance
    '''
    class Meta:
        model = Book
        fields = ['url', 'book_title', 'author', 'year', 'featured']


class UserListInstanceSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Basic list serializer for User model, view filters to only User model username
    '''
    class Meta:
        model = User
        fields = ['username', 'last_name']


# class UserListInstanceSerializer(serializers.HyperlinkedModelSerializer):
#     '''
#     Basic list serializer for User model, view filters to only User model username
#     '''
#     class Meta:
#         model = User
#         fields = ['username', 'last_name']

# need to add public notes and filter for only username?


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    '''
    User profile serializer with all User model info
    '''
    class Meta:
        model = User
        exclude = ['password']
# need to add public and private notes and books and restrict permissions so that only user can see their profile


class FeaturedBooksSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Serializer to display 'featured' books list filtered via view with boolean(featured=True)
    '''
    class Meta:
        model = Book
        fields = ['url', 'book_title', 'author', 'featured']


# class UserReadSerializer(serializers.HyperlinkedModelSerializer):
#     '''
#     Serializer to display book user has read
#     '''

#     class Meta:
#         model = Status
#         fields = ['read', 'user', 'book']


# class UserReadingSerializer(serializers.HyperlinkedModelSerializer):
#     '''
#     Serializer to display book user is reading
#     '''
#     class Meta:
#         model = Status
#         fields = ['reading', 'user', 'book']


# class UserWantToReadSerializer(serializers.HyperlinkedModelSerializer):
#     '''
#     Serializer to display book user wants to read
#     '''
#     class Meta:
#         model = Status
#         fields = ['want_to_read', 'user', 'book']
