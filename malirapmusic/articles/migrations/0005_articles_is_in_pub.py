# Generated by Django 3.0 on 2020-12-13 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20201213_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='is_in_pub',
            field=models.BooleanField(default=False, verbose_name='Is in pub'),
        ),
    ]
