# Generated by Django 4.1.7 on 2023-03-11 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0016_alter_commentary_pk_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentary',
            name='commentator',
        ),
    ]
