# Generated by Django 3.1 on 2021-02-23 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0041_auto_20210223_0521'),
    ]

    operations = [
        migrations.AddField(
            model_name='bundesliga',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='info.englishclubs'),
        ),
    ]
