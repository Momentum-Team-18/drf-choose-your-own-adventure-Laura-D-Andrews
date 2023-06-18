# Generated by Django 4.2.2 on 2023-06-18 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0014_rename_username_note_commenter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='note_title',
            new_name='note_title_private',
        ),
        migrations.AddField(
            model_name='note',
            name='note_title_public',
            field=models.CharField(default=1, max_length=100, verbose_name='title'),
            preserve_default=False,
        ),
    ]
