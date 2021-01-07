from django.contrib import admin
from .models import scrapdata
# Register your models here.

class movieInLine(admin.ModelAdmin):
    model = scrapdata
    extra = 0
    ordering = ('title',)

admin.site.register(scrapdata,movieInLine)

