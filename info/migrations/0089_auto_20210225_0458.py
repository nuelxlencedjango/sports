# Generated by Django 3.1 on 2021-02-25 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0088_auto_20210225_0406'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bundesliga',
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
            model_name='premiership',
            name='league',
        ),
        migrations.RemoveField(
            model_name='turkey',
            name='league',
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
            name='Premiership',
        ),
        migrations.DeleteModel(
            name='Turkey',
        ),
    ]
