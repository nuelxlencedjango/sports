# Generated by Django 3.1 on 2021-02-25 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0085_auto_20210225_0404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bundesliga',
            name='win',
            field=models.CharField(default='bund', max_length=50, unique=True),
        ),
    ]
