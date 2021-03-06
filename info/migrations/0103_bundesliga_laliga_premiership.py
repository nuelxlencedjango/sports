# Generated by Django 3.1 on 2021-02-25 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0102_auto_20210225_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Premiership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('played', models.IntegerField()),
                ('win', models.IntegerField()),
                ('draw', models.IntegerField()),
                ('lost', models.IntegerField()),
                ('goalf', models.IntegerField()),
                ('goala', models.IntegerField()),
                ('team_name', models.CharField(max_length=50)),
                ('point', models.IntegerField(default=0)),
                ('league', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='info.league', verbose_name='League')),
            ],
            options={
                'verbose_name_plural': 'Premiership',
            },
        ),
        migrations.CreateModel(
            name='Laliga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('played', models.IntegerField()),
                ('win', models.IntegerField()),
                ('draw', models.IntegerField()),
                ('lost', models.IntegerField()),
                ('goalf', models.IntegerField()),
                ('goala', models.IntegerField()),
                ('team_name', models.CharField(max_length=50)),
                ('point', models.IntegerField(default=0)),
                ('league', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='info.league', verbose_name='League')),
            ],
            options={
                'verbose_name_plural': 'Laliga',
            },
        ),
        migrations.CreateModel(
            name='Bundesliga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('played', models.IntegerField()),
                ('win', models.IntegerField()),
                ('draw', models.IntegerField()),
                ('lost', models.IntegerField()),
                ('goalf', models.IntegerField()),
                ('goala', models.IntegerField()),
                ('team_name', models.CharField(max_length=50)),
                ('point', models.IntegerField(default=0)),
                ('league', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='info.league', verbose_name='League')),
            ],
            options={
                'verbose_name_plural': 'Bundesliga',
            },
        ),
    ]
