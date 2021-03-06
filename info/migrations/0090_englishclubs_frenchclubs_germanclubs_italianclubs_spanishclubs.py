# Generated by Django 3.1 on 2021-02-25 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0089_auto_20210225_0458'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnglishClubs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'EnglishClubs',
            },
        ),
        migrations.CreateModel(
            name='FrenchClubs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'FrenchClubs',
            },
        ),
        migrations.CreateModel(
            name='GermanClubs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'GermanClubs',
            },
        ),
        migrations.CreateModel(
            name='ItalianClubs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'ItalianClubs',
            },
        ),
        migrations.CreateModel(
            name='SpanishClubs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'SpanishClubs',
            },
        ),
    ]
