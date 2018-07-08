# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from .forms import AddJobForm 
from .forms import SearchForm 

from .models import SignUp
from .models import Job
from .models import Apply
from .models import Search



# Create your views here.
def home(request):
	title = "SignUp Now"
	context = { "title":title }	
	return render(request,'app2/home.html',context)

 # def jobs(request):
	# form = JobForm(request.POST or None)
	# context = { "form":form }
	# if form.is_valid():
	# 	instance = form.save(commit=False)
	# 	job_id = form.cleaned_data.get("job_id")
	# 	job_title = form.cleaned_data.get("job_title")
	# 	instance.save()
	# return render(request,'app2/jobs.html',context)

def applied_jobs(request):
	userid = request.user.id
	user = Apply.objects.get(userid = userid)
	print user
	applied_jobs = (user.apply_job).all()
	context = {
	"applied_jobs":applied_jobs
	}
	return render(request,'app2/applied.html',context)


def add_job(request):
	if Job.objects.count()==0 or Job.objects.count()== None:
		job_id = "JOBNO0"
	else:
		job_id = "JOBNO"+str(Job.objects.count())
	if request.method == "POST":
		form = AddJobForm(request.POST)
		if form.is_valid():
			job_title= form.cleaned_data["job_title"]
			description = form.cleaned_data["description"]
			company_name = form.cleaned_data["company_name"]
			qualification = form.cleaned_data["qualification"]
			email = form.cleaned_data["email"]
			# form.cleaned_data["job_id"] = request.user.id
			instance = Job(
				job_title=job_title,
				description = description,
				company_name = company_name,
				qualification = qualification,
				email = email,
				job_id = job_id
				)
			instance.save()
		return HttpResponseRedirect(reverse("add_job"))

	else:
		form = AddJobForm()
		context = {
		"form": form,
		"job_id":job_id
		}
		return render(request,'app2/add_job.html',context)

def view_jobs(request):
	queryset = Job.objects.all()
	# userid = request.user.id
	try:
		userid = request.user.id
		user = Apply.objects.get(userid = userid)
		print user
		applied_jobs = (user.apply_job).all()
		context = {
		"queryset":queryset,
		"applied_jobs":applied_jobs
		}
		return render(request,'app2/view_job.html',context)
	except:
		context = {
		"queryset":queryset,
		}
		return render(request,'app2/view_job.html',context)

def apply(request,pk):
	# query = Job.objects.get(id=pk)
	userid = request.user.id
	job = Job.objects.get(pk=pk)

	if Apply.objects.filter(userid = userid):
		instance = Apply.objects.get(userid = userid)
	else:
		instance = Apply(
		userid = userid
		)
		instance.save()
	# print(job.job_title,job)
	
	instance.apply_job.add(job)
	
	
	return HttpResponseRedirect(reverse("view_jobs"))


def delete(request,pk):
	userid = request.user.id
	instance = Apply.objects.get(userid = userid)
	# print instance,pk
	job = Job.objects.get(pk=pk)

	instance.apply_job.remove(job)
	instance.save()
	# print instance.apply_job.all()
	return HttpResponseRedirect(reverse("view_jobs"))

def search(request):
	
	form = SearchForm()
	context ={"form":form}
	return render(request,'app2/search.html',context)
	# return HttpResponseRedirect(reverse("search"))