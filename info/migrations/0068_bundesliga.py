# Generated by Django 3.1 on 2021-02-24 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0067_auto_20210224_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bundesliga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Bundesliga',
            },
        ),
    ]
