# Generated by Django 3.1 on 2021-02-25 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0083_delete_bundesliga'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bundesliga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(default='bund', max_length=50, unique=True)),
                ('league', models.CharField(max_length=30)),
                ('played', models.IntegerField()),
                ('win', models.IntegerField()),
                ('draw', models.IntegerField()),
                ('lost', models.IntegerField()),
                ('goalf', models.IntegerField()),
                ('goala', models.IntegerField()),
                ('point', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Bundesliga',
            },
        ),
    ]
