# Generated by Django 4.2.2 on 2023-06-19 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_status_read_alter_status_reading_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='notes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='notes_related_to_book', to='library.note'),
            preserve_default=False,
        ),
    ]
