# Generated by Django 4.2.2 on 2023-06-15 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='notes',
        ),
    ]