from django.contrib import admin

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin

from articleapp.models import Article

class ArticleAdmin(SummernoteModelAdmin):
    search_fields = ['title',  'content', 'created_at']
    summernote_fields = '__all__'


admin.site.register(Article, ArticleAdmin)