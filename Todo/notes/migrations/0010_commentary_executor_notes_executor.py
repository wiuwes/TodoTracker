# Generated by Django 4.1.7 on 2023-03-10 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0009_alter_notes_process'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentary',
            name='executor',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='notes',
            name='executor',
            field=models.CharField(max_length=100, null=True),
        ),
    ]