# Generated by Django 3.0 on 2020-12-17 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20201217_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='fields',
            field=models.CharField(choices=[('Actu Buzz', 'ACTU BUZZ'), ('Albums', 'ALBUMS'), ('Singles', 'SINGLES'), ('Videos', 'VIDEOS'), ('Others', 'OTHERS')], max_length=100, unique=True, verbose_name='Category fields'),
        ),
    ]
