# Generated by Django 2.1.5 on 2020-05-09 15:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190124_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 9, 15, 54, 11, 822063), verbose_name='date published'),
        ),
    ]
