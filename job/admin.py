from django.contrib import admin
from .models import Job, Tag, JobSearch, JobApplication


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

@admin.register(JobSearch)
class JobSearchsAdmin(admin.ModelAdmin):

    list_display = [field.name for field in JobSearch._meta.fields]

    list_display_links = ["job_search_title"]

    search_fields = ["job_search_title"]

    list_filter = ["created_date"]
    class Meta:
        model = JobSearch


@admin.register(JobApplication)
class JobApplicationsAdmin(admin.ModelAdmin):

    list_display = [field.name for field in JobApplication._meta.fields]

    list_display_links = ["job"]

    search_fields = ["job"]

    list_filter = ["created_date"]
    class Meta:
        model = JobApplication