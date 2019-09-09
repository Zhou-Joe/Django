# Generated by Django 2.1.8 on 2019-09-07 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190905_2046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorialseries',
            name='tutorial_category',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='tutorial_series',
        ),
        migrations.AddField(
            model_name='tutorial',
            name='model_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.TutorialCategory', verbose_name='Category'),
        ),
        migrations.DeleteModel(
            name='TutorialSeries',
        ),
    ]