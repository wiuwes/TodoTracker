# Generated by Django 4.1.6 on 2023-03-08 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_alter_notes_process'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='process',
            field=models.CharField(choices=[('0', 'open'), ('1', 'in process'), ('2', 'verefication needed'), ('3', 'close')], default='0', max_length=1),
        ),
    ]
