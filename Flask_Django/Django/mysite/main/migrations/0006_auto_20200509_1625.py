# Generated by Django 2.1.5 on 2020-05-09 16:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200509_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 9, 16, 25, 35, 722738), verbose_name='date published'),
        ),
    ]