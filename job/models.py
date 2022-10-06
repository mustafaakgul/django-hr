from django.db import models
from ckeditor.fields import RichTextField


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


class Jobs(models.Model):
    jobs_creator = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Creator")
    job_title = models.CharField(max_length=50)
    job_description = models.TextField(max_length=2000)
    job_location = models.CharField(max_length=50, choices=LOCATIONS)
    job_department = models.CharField(max_length=50, choices=DEPARTMENTS)
    job_type = models.CharField(max_length=50, choices=JOB_TYPES)
    # tags = models.ManyToManyField(Tag, blank=True)
    applicant = models.ManyToManyField("auth.User", null=True, blank=True, related_name="applicant")
    status = models.CharField(max_length=50, choices=STATUS)
    job_slug = models.SlugField(unique=True, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.job_name

#
# class CaseCommon(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User")
#     case_name = models.CharField(max_length=50)
#     currency_type = models.CharField(max_length=50, choices=CASE_TYPE, default=CASE_TYPE[0][0])
#     initial_balance = models.DecimalField(max_digits=13, decimal_places=4, blank=True, null=True, default=0)
#     case_date = models.DateTimeField(default=timezone.now)
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_date = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         abstract = True
#         ordering = ['-created_date']
#
#     def __str__(self):
#         return self.case_name
#
#
# class Case(CaseCommon):
#
#     class Meta:
#         ordering = ['-created_date']
#
#     def __str__(self):
#         return self.case_name
#
#
# class CaseDeleted(CaseCommon):
#     old_model_created_date = models.DateTimeField(blank=True, null=True)
#     old_model_update_date = models.DateTimeField(blank=True, null=True)
#
#
#     class Meta:
#         ordering = ['-created_date']
#
#     def __str__(self):
#         return self.case_name
#
#
# class CaseArchieved(CaseCommon):
#     old_model_created_date = models.DateTimeField(blank=True, null=True)
#     old_model_update_date = models.DateTimeField(blank=True, null=True)
#
#
#     class Meta:
#         ordering = ['-created_date']
#
#     def __str__(self):
#         return self.case_name