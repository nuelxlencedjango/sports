# Generated by Django 3.1 on 2021-02-22 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0037_auto_20210222_2139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bundesliga',
            old_name='League',
            new_name='league',
        ),
        migrations.RenameField(
            model_name='italianseriea',
            old_name='League',
            new_name='league',
        ),
        migrations.RenameField(
            model_name='laliga',
            old_name='League',
            new_name='league',
        ),
        migrations.RenameField(
            model_name='ligue1',
            old_name='League',
            new_name='league',
        ),
        migrations.RenameField(
            model_name='premiership',
            old_name='League',
            new_name='league',
        ),
        migrations.AlterField(
            model_name='bundesliga',
            name='draw',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bundesliga',
            name='goala',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bundesliga',
            name='goalf',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bundesliga',
            name='lost',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bundesliga',
            name='played',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bundesliga',
            name='win',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='italianseriea',
            name='draw',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='italianseriea',
            name='goala',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='italianseriea',
            name='goalf',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='italianseriea',
            name='lost',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='italianseriea',
            name='played',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='italianseriea',
            name='win',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='laliga',
            name='draw',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='laliga',
            name='goala',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='laliga',
            name='goalf',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='laliga',
            name='lost',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='laliga',
            name='played',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='laliga',
            name='win',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ligue1',
            name='draw',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ligue1',
            name='goala',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ligue1',
            name='goalf',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ligue1',
            name='lost',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ligue1',
            name='played',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ligue1',
            name='win',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='premiership',
            name='draw',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='premiership',
            name='goala',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='premiership',
            name='goalf',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='premiership',
            name='lost',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='premiership',
            name='played',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='premiership',
            name='win',
            field=models.IntegerField(),
        ),
    ]
