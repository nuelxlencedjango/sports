# Generated by Django 3.1 on 2021-02-18 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0021_italianseriea'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laliga',
            name='team_name',
        ),
        migrations.RemoveField(
            model_name='ligue1',
            name='team_name',
        ),
        migrations.RemoveField(
            model_name='premiership',
            name='team_name',
        ),
        migrations.DeleteModel(
            name='Bundesliga',
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
    ]
