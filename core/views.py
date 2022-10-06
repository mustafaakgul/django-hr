from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "index.html")


@login_required(login_url="accounts:login")
def dashboard(request):
    return render(request, "dashboard.html")
