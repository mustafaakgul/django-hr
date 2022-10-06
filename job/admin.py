from django.contrib import admin
from .models import Jobs


@admin.register(Jobs)
class JobsAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Jobs._meta.fields]

    list_display_links = ["job_title"]

    search_fields = ["job_title"]

    list_filter = ["created_date"]
    class Meta:
        model = Jobs

