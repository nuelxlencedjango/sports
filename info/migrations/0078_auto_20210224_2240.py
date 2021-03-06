# Generated by Django 3.1 on 2021-02-24 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0077_delete_premiers'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnglishClubs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'EnglishClubs',
            },
        ),
        migrations.CreateModel(
            name='FrenchClubs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'FrenchClubs',
            },
        ),
        migrations.CreateModel(
            name='GermanClubs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'GermanClubs',
            },
        ),
        migrations.CreateModel(
            name='ItalianClubs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'ItalianClubs',
            },
        ),
        migrations.CreateModel(
            name='SpanishClubs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'SpanishClubs',
            },
        ),
        migrations.CreateModel(
            name='TurkishClubs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='italianseriea',
            options={'verbose_name_plural': 'ItalianSerieA'},
        ),
        migrations.AlterField(
            model_name='italianseriea',
            name='point',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ligue1',
            name='point',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='premiership',
            name='point',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='turkey',
            name='point',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bundesliga',
            name='team_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='info.germanclubs'),
        ),
        migrations.AlterField(
            model_name='italianseriea',
            name='team_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='info.italianclubs'),
        ),
        migrations.AlterField(
            model_name='laliga',
            name='team_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='info.spanishclubs'),
        ),
        migrations.AlterField(
            model_name='ligue1',
            name='team_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='info.frenchclubs'),
        ),
        migrations.AlterField(
            model_name='premiership',
            name='team_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='info.englishclubs'),
        ),
        migrations.AlterField(
            model_name='turkey',
            name='team_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='info.turkishclubs'),
        ),
    ]
