# Generated by Django 4.1.2 on 2022-10-06 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Jobs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("job_title", models.CharField(max_length=50)),
                ("job_description", models.TextField(max_length=2000)),
                (
                    "job_department",
                    models.CharField(
                        choices=[
                            (
                                "Electronic Manufacturing and Integration",
                                "Electronic Manufacturing and Integration",
                            ),
                            (
                                "Artificial Intelligence Software Technologies",
                                "Artificial Intelligence Software Technologies",
                            ),
                            (
                                "Electronic System Development",
                                "Electronic System Development",
                            ),
                            ("Web Software Technologies", "Web Software Technologies"),
                        ],
                        max_length=50,
                    ),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                (
                    "applicant",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="applicant",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "jobs_creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ["-created_date"],},
        ),
    ]