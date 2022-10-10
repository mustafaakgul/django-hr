# Generated by Django 4.1.2 on 2022-10-08 23:25

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("job", "0007_remove_jobsearch_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobapplication",
            name="cover_letter",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="jobapplication",
            name="resume",
            field=models.FileField(blank=True, null=True, upload_to="resume/"),
        ),
    ]