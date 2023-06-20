
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Book(models.Model):

    FEATURED_CHOICES = [(False, 'No'), (True, 'Yes')]

    book_title = models.CharField(max_length=100, verbose_name="title")
    author = models.CharField(max_length=100)
    featured = models.BooleanField(default=False, choices=FEATURED_CHOICES)
    year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.book_title


class Note(models.Model):

    PRIVACY_CHOICES = [(False, 'Private'), (True, 'Public')]

    commenter = models.ForeignKey(
        to='User', on_delete=models.CASCADE,
        related_name='notes_by_commenter')
    note_title = models.CharField(max_length=100)
    book = models.ForeignKey(
        to=Book, on_delete=models.CASCADE,
        related_name='notes_about_book')
    note_text = models.TextField(
        null=True, blank=True)
    privacy = models.BooleanField(
        default=False, null=True, blank=True, choices=PRIVACY_CHOICES)

    def __str__(self):
        return self.note_title


class User(AbstractUser):

    def __str__(self):
        return self.username


class Status(models.Model):

    STATUS_CHOICES = [(False, 'No'), (True, 'Yes')]

    follow_status = models.CharField(max_length=30, default='Follow Status')
    read = models.BooleanField(
        default=False, null=True, blank=True, choices=STATUS_CHOICES)
    reading = models.BooleanField(
        default=False, null=True, blank=True, choices=STATUS_CHOICES)
    want_to_read = models.BooleanField(
        default=False, verbose_name="Want to read", null=True, blank=True, choices=STATUS_CHOICES)
    user = models.ForeignKey(
        to='User', on_delete=models.CASCADE,
        related_name='user_relation_to_status')
    book = models.ForeignKey(
        to=Book, on_delete=models.CASCADE,
        related_name='book_status')

    def __str__(self):
        return self.follow_status
