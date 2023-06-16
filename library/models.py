
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Book(models.Model):
    FEATURED_CHOICES = [(False, 'No'), (True, 'Yes')]
    book_title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    featured = models.BooleanField(default=False, choices=FEATURED_CHOICES)
    year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.book_title


class Note(models.Model):
    user = models.ForeignKey(
        to='User', on_delete=models.CASCADE,
        related_name='user_related_to_note')
    note_title = models.CharField(max_length=100)
    book = models.ForeignKey(
        to=Book, on_delete=models.CASCADE,
        related_name='book_related_to_note')
    private_note_text = models.TextField(null=True, blank=True)
    public_note_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.note_title


class User(AbstractUser):
    following = models.ManyToManyField(Book, blank=True, null=True)
