# Generated by Django 3.1 on 2021-02-24 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0066_laliga_point'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='italianseriea',
            name='league',
        ),
        migrations.RemoveField(
            model_name='laliga',
            name='league',
        ),
        migrations.RemoveField(
            model_name='ligue1',
            name='league',
        ),
        migrations.RemoveField(
            model_name='turkey',
            name='league',
        ),
        migrations.DeleteModel(
            name='Bundesliga',
        ),
        migrations.DeleteModel(
            name='ItalianSerieA',
        ),
        migrations.DeleteModel(
            name='Laliga',
        ),
        migrations.DeleteModel(
            name='Ligue1',
        ),
        migrations.DeleteModel(
            name='Turkey',
        ),
    ]
