# Generated by Django 2.1.8 on 2019-09-07 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190907_0649'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('published', models.DateTimeField(verbose_name='date published')),
                ('cat_slug', models.CharField(default=1, max_length=200)),
                ('icon', models.ImageField(blank=True, upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=200)),
                ('slug', models.CharField(default=1, max_length=200)),
                ('img', models.ImageField(blank=True, upload_to='img')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='model_category',
        ),
        migrations.DeleteModel(
            name='Tutorial',
        ),
        migrations.DeleteModel(
            name='TutorialCategory',
        ),
        migrations.AddField(
            model_name='cat',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.Category', verbose_name='Category'),
        ),
    ]
