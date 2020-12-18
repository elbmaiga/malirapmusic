# Generated by Django 3.0 on 2020-12-17 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_galleries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='fields',
            field=models.CharField(choices=[('Actu Buzz', 'ACTU BUZZ'), ('Album', 'ALBUM'), ('Single', 'SINGLE'), ('Video', 'VIDEO'), ('Other', 'OTHER')], max_length=100, unique=True, verbose_name='Category fields'),
        ),
    ]
