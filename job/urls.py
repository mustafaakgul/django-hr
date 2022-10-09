from django.urls import path
from .views import *

app_name = "job"

urlpatterns = [
    path('list-jobs/', list_jobs,name = "list_jobs"),
    path('apply-jobs/<int:id>', apply_jobs, name="apply_jobs"),
    path('list-personalized-jobs/', personalized_jobs, name="personalized_jobs")
]