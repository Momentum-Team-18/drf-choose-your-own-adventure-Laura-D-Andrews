from .models import User, Book, Note
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
    Basic serializer for User model, objects.all queryset, links to user list and user instance
    '''
    class Meta:
        model = User
        read_only_fields = ['__all__']
        exclude = ['password']
