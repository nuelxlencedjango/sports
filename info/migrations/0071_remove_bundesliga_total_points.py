# Generated by Django 3.1 on 2021-02-24 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0070_bundesliga'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bundesliga',
            name='total_points',
        ),
    ]