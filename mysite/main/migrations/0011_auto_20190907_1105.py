# Generated by Django 2.1.8 on 2019-09-07 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20190907_0755'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cat',
            old_name='published',
            new_name='birthday',
        ),
    ]
