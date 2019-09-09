from django.db import models
from datetime import datetime


# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=200, unique=True)
    summary = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, default=1)
    img = models.ImageField(upload_to='img',blank=True)


    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category




class Cat(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.DateTimeField('date published')
    # https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.ForeignKey.on_delete
    cat_category = models.ForeignKey(Category, to_field='category',default=1, verbose_name="Categories", on_delete=models.SET_DEFAULT)
    slug = models.CharField(max_length=200, default=1)
    icon=models.ImageField(upload_to='img',blank=True)
    birth=models.DateField('Birthday',default=datetime.today)

    def __str__(self):
        return self.title
