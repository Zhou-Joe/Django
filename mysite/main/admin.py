from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.
from .models import Tutorial, TutorialSeries, TutorialCategory


class TutorialAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {'fields': ["title", "published"]}),
        ("URL", {'fields': ["tutorial_slug"]}),
        ("Series", {'fields': ["tutorial_series"]}),
        ("Content", {"fields": ["content"]}),
        ("Icon",{"fields": ["icon"]})
    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
admin.site.register(Tutorial, TutorialAdmin)