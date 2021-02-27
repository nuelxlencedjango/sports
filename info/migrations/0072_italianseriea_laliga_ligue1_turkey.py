# Generated by Django 3.1 on 2021-02-24 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0071_remove_bundesliga_total_points'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turkey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=50, unique=True)),
                ('played', models.IntegerField()),
                ('win', models.IntegerField()),
                ('draw', models.IntegerField()),
                ('lost', models.IntegerField()),
                ('goalf', models.IntegerField()),
                ('goala', models.IntegerField()),
                ('point', models.IntegerField()),
                ('league', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='info.league', verbose_name='League')),
            ],
            options={
                'verbose_name_plural': 'Turkey',
            },
        ),
        migrations.CreateModel(
            name='Ligue1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=50, unique=True)),
                ('played', models.IntegerField()),
                ('win', models.IntegerField()),
                ('draw', models.IntegerField()),
                ('lost', models.IntegerField()),
                ('goalf', models.IntegerField()),
                ('goala', models.IntegerField()),
                ('point', models.IntegerField()),
                ('league', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='info.league', verbose_name='League')),
            ],
            options={
                'verbose_name_plural': 'Ligue1',
            },
        ),
        migrations.CreateModel(
            name='Laliga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=50, unique=True)),
                ('played', models.IntegerField()),
                ('win', models.IntegerField()),
                ('draw', models.IntegerField()),
                ('lost', models.IntegerField()),
                ('goalf', models.IntegerField()),
                ('goala', models.IntegerField()),
                ('point', models.IntegerField(default=0)),
                ('league', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='info.league', verbose_name='League')),
            ],
            options={
                'verbose_name_plural': 'Laliga',
            },
        ),
        migrations.CreateModel(
            name='ItalianSerieA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=50, unique=True)),
                ('played', models.IntegerField()),
                ('win', models.IntegerField()),
                ('draw', models.IntegerField()),
                ('lost', models.IntegerField()),
                ('goalf', models.IntegerField()),
                ('goala', models.IntegerField()),
                ('point', models.IntegerField()),
                ('league', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='info.league', verbose_name='League')),
            ],
            options={
                'verbose_name_plural': 'ItalianSerie A',
            },
        ),
    ]
