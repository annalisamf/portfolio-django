from django.shortcuts import render, get_object_or_404

from .models import Job


# Create your views here.
def home(request):
    jobs = Job.objects
    # passing also the list of jobs in the render
    return render(request, 'jobs/home.html', {'jobs': jobs})


def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)  # pk is primary key
    return render(request, 'jobs/detail.html', {'job': job_detail})
