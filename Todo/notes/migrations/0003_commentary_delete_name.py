# Generated by Django 4.1.6 on 2023-03-05 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=100)),
                ('commentary', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Name',
        ),
    ]
