from django.contrib import admin

from app.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("content",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name",)
