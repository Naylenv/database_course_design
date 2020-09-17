from django.contrib import admin
from .models import *


class DiscussAdmin(admin.ModelAdmin):
    list_display = ['discuss_id', 'text', 'student', 'like_num']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_id', 'discuss', 'text', 'student']


admin.site.register(Comment, CommentAdmin)
admin.site.register(Discuss, DiscussAdmin)
# Register your models here.
