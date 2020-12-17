from django.contrib import admin

# Register your models here.

from .models import *

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'views', 'download')

admin.site.register(Articles, ArticleAdmin)
admin.site.register(Category)
admin.site.register(File_Uploaded)
admin.site.register(Galleries)