# Generated by Django 4.2.2 on 2023-06-15 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_alter_book_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='status',
        ),
        migrations.RemoveField(
            model_name='user',
            name='status',
        ),
    ]