# Generated by Django 4.1.2 on 2022-10-08 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("job", "0002_tag_jobs_deleted_date_jobs_job_location_and_more"),
    ]

    operations = [
        migrations.RenameModel(old_name="Tag", new_name="Tags",),
    ]