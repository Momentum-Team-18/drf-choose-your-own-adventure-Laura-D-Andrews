
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Book(models.Model):
    FEATURED_CHOICES = [(False, 'No'), (True, 'Yes')]
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    featured = models.BooleanField(default=False, choices=FEATURED_CHOICES)

    def __str__(self):
        return self.title


class User(AbstractUser):
    books = models.ManyToManyField(Book, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)


class Note(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    book = models.ForeignKey(
        to=Book, on_delete=models.CASCADE, related_name='book_note')
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="user_note",
        blank=True, null=True)

    STATUS_CHOICES = [(False, 'Public'), (True, 'Private')]
    status = models.BooleanField(default=True, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title
