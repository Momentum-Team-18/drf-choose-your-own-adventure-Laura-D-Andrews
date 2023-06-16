# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from rest_framework.decorators import action
from rest_framework import permissions, renderers, viewsets, generics
# from rest_framework.response import Response
from .models import User, Book, Note
from library.permissions import IsOwnerOrReadOnly
from library.serializers import UserSerializer, BookSerializer, NoteSerializer, UserNoteSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [
        permissions.IsAuthenticated]


class UserNoteViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserNoteSerializer
    # permission_classes = [
    #     permissions.IsAuthenticated]
