from .models import User, Book, Note
from rest_framework import serializers


class BookSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Book
        fields = ['title', 'author', 'featured']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # books = serializers.RelatedField(many=True)
    note = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'note', 'private']


class NoteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Note
        fields = ['book', 'title', 'text']
