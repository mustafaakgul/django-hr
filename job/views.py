from django.shortcuts import render
from .models import Job, JobSearch, JobApplication, Tag
from django.shortcuts import get_object_or_404
from accounts.models import Account
from django.db import transaction, IntegrityError


def list_jobs(request):
    keyword = request.GET.get("keyword")
    if keyword:
        try:
            with transaction.atomic():
                jobs = Job.objects.filter(job_title__icontains= keyword)

                job_search = JobSearch.objects.create(
                    job_search_title=keyword,
                )
                job_search.searcher.add(request.user)
                job_search.save()

                tags = Tag.objects.filter(name__icontains=keyword)
                for tag in tags:
                    tag.tags_related.add(request.user)
                    tag.save()

                context = {
                    "jobs": jobs
                }
                return render(request, 'jobs/list-jobs.html', context)
        except IntegrityError:
            # Sentry Logging
            #logger.error('Invoice NOT CREATED: ', request.user.username)
            pass

    jobs = Job.objects.all()
    context = {
        "jobs": jobs
    }
    return render(request, 'jobs/list-jobs.html', context)


def apply_jobs(request, id):
    job = get_object_or_404(Job, id=id)
    job_app = JobApplication.objects.create(
        job=job,
        applicant=request.user
    )
    job_app.save()
    context = {
        "job": job
    }
    return render(request, 'jobs/list-jobs.html', context)


def personalized_jobs(request):
    # jobs = Job.objects.filter(tags__in=request.user.tags.all())
    # context = {
    #     "jobs": jobs
    # }
    # return render(request, 'jobs/list-jobs.html', context)
    account = Account.objects.get(id=request.user.id)
    tags = account.tags.all()
    jobs = Job.objects.filter(tags__in=tags)
    context = {
        "jobs": jobs
    }
    return render(request, 'jobs/personalized_jobs.html', context)