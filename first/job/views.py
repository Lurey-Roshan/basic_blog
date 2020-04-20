from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from job.models import Job

def job_index(request):
	job=Job.objects.all()
	context={ 
	'job':job
	}
	return render(request, 'job/job_index.html', context)


def job_detail(request, pk):
	job = Job.objects.get(pk=pk)
	context={
		'job':job
	}
	return render( request, 'job/job_detail.html', context)
	
