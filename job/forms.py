from django import forms
from .models import Jobs


class JobsForm(forms.ModelForm):
    class Meta:

        model = Jobs

        fields = [
            "job_title",
            "job_description",
            "job_location",
            "job_type",
            "job_slug"
        ]