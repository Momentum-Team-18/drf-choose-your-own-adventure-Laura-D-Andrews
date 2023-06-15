
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Book(models.Model):
    FEATURED_CHOICES = [(False, 'No'), (True, 'Yes')]
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    featured = models.BooleanField(default=False, choices=FEATURED_CHOICES)
    # followers = models.TextField()

    def __str__(self):
        return self.title


class Note(models.Model):
    NOTE_CHOICES = [(False, 'Public'), (True, 'Private')]
    private = models.BooleanField(default=True, choices=NOTE_CHOICES)
    title = models.CharField(max_length=100)
    text = models.TextField()
    book = models.ForeignKey(
        to=Book, on_delete=models.CASCADE, related_name='book_note')

    def __str__(self):
        return self.title


class User(AbstractUser):
    private = models.ForeignKey(
        to=Note, on_delete=models.CASCADE, related_name='private_note')
    notes = models.ForeignKey(
        to=Note, on_delete=models.CASCADE, related_name='notes')
    books = models.ManyToManyField(Book)
    # follow_list = models.TextField()
