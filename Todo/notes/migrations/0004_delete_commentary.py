# Generated by Django 4.1.7 on 2023-03-05 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_commentary_delete_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Commentary',
        ),
    ]
