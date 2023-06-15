from .models import User, Book, Note
from rest_framework import serializers


class BookSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Book
        fields = ['url', 'title', 'author', 'featured']


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    private = serializers.ChoiceField(Note.STATUS_CHOICES)

    class Meta:
        model = Note
        fields = ['url', 'book', 'title', 'text', 'private']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    notes = NoteSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'notes', 'following']
