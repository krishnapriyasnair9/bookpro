# Generated by Django 4.0.3 on 2022-03-22 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookadd', '0004_rename_book_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
