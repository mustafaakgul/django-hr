from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings


DEPARTMENTS = [
    ('Electronic Manufacturing and Integration', 'Electronic Manufacturing and Integration'),
    ('Artificial Intelligence Software Technologies', 'Artificial Intelligence Software Technologies'),
    ('Electronic System Development', 'Electronic System Development'),
    ('Web Software Technologies', 'Web Software Technologies')
]

LOCATIONS = [
    ('Istanbul', 'Istanbul'),
    ('Ankara', 'Ankara'),
    ('Edirne', 'Edirne'),
]

JOB_TYPES = [
    ('Full Time Remote', 'Full Time Remote'),
    ('Full Time Hybrid', 'Full Time Hybrid'),
    ('Full Time On Site', 'Full Time On Site'),
    ('Part Time', 'Part Time'),
    ('Internship', 'Internship'),
    ('Freelance', 'Freelance'),
    ('Temporary', 'Temporary'),
]

STATUS = [
    ('Active', 'Active'),
    ('Passive', 'Passive'),
    ('Deleted', 'Deleted'),
    ('Archived', 'Archived'),
]


class Tag(models.Model):
    name = models.CharField(max_length=50)

    status = models.CharField(max_length=50, choices=STATUS, default=STATUS[0][0])
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    jobs_creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Creator")
    job_title = models.CharField(max_length=50)
    job_description = models.TextField(max_length=2000)
    job_location = models.CharField(max_length=50, choices=LOCATIONS, default=LOCATIONS[0][0])
    job_department = models.CharField(max_length=50, choices=DEPARTMENTS)
    job_type = models.CharField(max_length=50, choices=JOB_TYPES, default=JOB_TYPES[0][0])
    tags = models.ManyToManyField(Tag, blank=True, null=True, related_name='jobs')
    applicant = models.ManyToManyField(settings.AUTH_USER_MODEL, null=True, blank=True, related_name="applicant")
    #job_slug = models.SlugField(unique=True, editable=False)

    status = models.CharField(max_length=50, choices=STATUS, default=STATUS[0][0])
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.job_title


class JobSearch(models.Model):
    job_search_title = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag, blank=True, null=True, related_name='search_tags')
    searcher = models.ManyToManyField(settings.AUTH_USER_MODEL, null=True, blank=True, related_name="searcher")

    status = models.CharField(max_length=50, choices=STATUS, default=STATUS[0][0])
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.job_search_title


class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, verbose_name="Job")
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Applicant")
    cover_letter = RichTextField()
    resume = models.FileField(upload_to='resume/')

    status = models.CharField(max_length=50, choices=STATUS, default=STATUS[0][0])
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.job.job_title