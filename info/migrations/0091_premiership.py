# Generated by Django 3.1 on 2021-02-25 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0090_englishclubs_frenchclubs_germanclubs_italianclubs_spanishclubs'),
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
                ('total_points', models.IntegerField()),
                ('point', models.IntegerField(default=0)),
                ('league', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='info.league', verbose_name='League')),
                ('team_name', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='info.englishclubs')),
            ],
            options={
                'verbose_name_plural': 'Premiership',
            },
        ),
    ]
