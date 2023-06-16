from .models import User, Book, Note
from rest_framework import serializers


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    private = serializers.ChoiceField(Note.STATUS_CHOICES)

    class Meta:
        model = Note
        fields = ['url', 'book', 'note_title', 'text', 'user', 'private']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    note_title = NoteSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'following', 'note_title']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    note_title = NoteSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['url', 'title', 'note_title', 'author']


class UserNoteSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Serializer to nest/display user-specific notes on the User instance
    '''
    note_title = NoteSerializer(read_only=True)
    # note_title = NoteSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['note_title']
