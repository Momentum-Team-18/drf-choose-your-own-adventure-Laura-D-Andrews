
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Book(models.Model):
    FEATURED_CHOICES = [(False, 'No'), (True, 'Yes')]

    READ = 'Read'
    READING = 'Reading'
    WANT_TO_READ = "Want to read"
    # DJANGOFILTERBACKEND
    # NOT_INTERESTED = 'Not interested'
    # STATUS_CHOICES = [(READ, 'Read'), (READING, 'Reading'),
    #                   (WANT_TO_READ, 'Want to read'), (NOT_INTERESTED, 'Not interest')]
    # status = models.ChoiceField(null=True, blank=True, choices=STATUS_CHOICES)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    featured = models.BooleanField(default=False, choices=FEATURED_CHOICES)

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
    books = models.ManyToManyField(Book)
    private = models.ForeignKey(
        to=Note, on_delete=models.CASCADE, related_name='private_note')
    owner = models.ForeignKey(
        to=Note, on_delete=models.CASCADE, related_name='note_owner')
