# Generated by Django 3.1 on 2021-02-22 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0033_auto_20210222_0916'),
    ]

    operations = [
        migrations.CreateModel(
            name='Premiership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league', models.CharField(max_length=50)),
                ('played', models.CharField(max_length=2)),
                ('win', models.CharField(max_length=2)),
                ('draw', models.CharField(max_length=2)),
                ('lost', models.CharField(max_length=2)),
                ('goalf', models.CharField(max_length=3)),
                ('goala', models.CharField(max_length=3)),
                ('total_points', models.CharField(max_length=3)),
                ('team_name', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='info.englishclubs')),
            ],
            options={
                'verbose_name_plural': 'Premiership',
            },
        ),
        migrations.CreateModel(
            name='Ligue1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league', models.CharField(max_length=50)),
                ('played', models.CharField(max_length=2)),
                ('win', models.CharField(max_length=2)),
                ('draw', models.CharField(max_length=2)),
                ('lost', models.CharField(max_length=2)),
                ('goalf', models.CharField(max_length=3)),
                ('goala', models.CharField(max_length=3)),
                ('total_points', models.CharField(max_length=3)),
                ('team_name', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='info.frenchclubs')),
            ],
            options={
                'verbose_name_plural': 'Ligue1',
            },
        ),
        migrations.CreateModel(
            name='Laliga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league', models.CharField(max_length=50)),
                ('played', models.CharField(max_length=2)),
                ('win', models.CharField(max_length=2)),
                ('draw', models.CharField(max_length=2)),
                ('lost', models.CharField(max_length=2)),
                ('goalf', models.CharField(max_length=3)),
                ('goala', models.CharField(max_length=3)),
                ('total_points', models.CharField(max_length=3)),
                ('team_name', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='info.spanishclubs')),
            ],
            options={
                'verbose_name_plural': 'Laliga',
            },
        ),
        migrations.CreateModel(
            name='ItalianSerieA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league', models.CharField(max_length=50)),
                ('played', models.CharField(max_length=2)),
                ('win', models.CharField(max_length=2)),
                ('draw', models.CharField(max_length=2)),
                ('lost', models.CharField(max_length=2)),
                ('goalf', models.CharField(max_length=3)),
                ('goala', models.CharField(max_length=3)),
                ('total_points', models.CharField(max_length=3)),
                ('team_name', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='info.italianclubs')),
            ],
            options={
                'verbose_name_plural': 'ItalianSerieA',
            },
        ),
        migrations.CreateModel(
            name='Bundesliga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league', models.CharField(max_length=50)),
                ('played', models.CharField(max_length=2)),
                ('win', models.CharField(max_length=2)),
                ('draw', models.CharField(max_length=2)),
                ('lost', models.CharField(max_length=2)),
                ('goalf', models.CharField(max_length=3)),
                ('goala', models.CharField(max_length=3)),
                ('total_points', models.CharField(max_length=3)),
                ('team_name', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='info.germanclubs')),
            ],
            options={
                'verbose_name_plural': 'Bundesliga',
            },
        ),
    ]
