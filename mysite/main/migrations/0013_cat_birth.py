# Generated by Django 2.1.8 on 2019-09-07 11:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20190907_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='birth',
            field=models.DateField(default=datetime.datetime.today, verbose_name='Birthday'),
        ),
    ]