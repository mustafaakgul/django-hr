from django.contrib import admin
from .models import Job, Tag


@admin.register(Job)
class JobsAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Job._meta.fields]

    list_display_links = ["job_title"]

    search_fields = ["job_title"]

    list_filter = ["created_date"]
    class Meta:
        model = Job


@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Tag._meta.fields]

    list_display_links = ["name"]

    search_fields = ["name"]

    list_filter = ["created_date"]
    class Meta:
        model = Tag

