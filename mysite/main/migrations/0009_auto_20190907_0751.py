# Generated by Django 2.1.8 on 2019-09-07 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20190907_0748'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cat',
            old_name='category',
            new_name='cat_category',
        ),
    ]
