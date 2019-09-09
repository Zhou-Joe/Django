from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.
from .models import Cat, Category


class TutorialAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {'fields': ["title", "published"]}),
        ("URL", {'fields': ["slug"]}),
        ("Content", {"fields": ["content","cat_category","birth"]}),

        ("Icon",{"fields": ["icon"]})
    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }



admin.site.register(Category)
admin.site.register(Cat, TutorialAdmin)