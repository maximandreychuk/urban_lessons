from django.contrib import admin
from .models import Task, Comment, Page


admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(Page)
