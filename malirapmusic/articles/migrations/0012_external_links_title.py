# Generated by Django 3.0 on 2020-12-18 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_auto_20201218_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='external_links',
            name='title',
            field=models.CharField(default='Test', max_length=255, verbose_name='Title'),
        ),
    ]
