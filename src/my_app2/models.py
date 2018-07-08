# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add =True,auto_now=False)
	updated = models.DateTimeField(auto_now_add =False,auto_now=True)
	def __unicode__(self):
		return self.email

class Job(models.Model):
	job_id =  models.CharField(max_length=120,blank=False,unique =True)
	job_title = models.CharField(max_length=120, blank=True, null=True)
	description = models.CharField(max_length=300, blank=True, null=True)
	company_name = models.CharField(max_length=120, blank=True, null=True)
	qualification = models.CharField(max_length=120, blank=True, null=True)
	email = models.EmailField()
	# userid =  models.CharField(max_length=120,blank=False)

	def __unicode__(self):
		return self.job_id

class Apply(models.Model):
	userid =  models.IntegerField(blank=False,unique = True)
	apply_job = models.ManyToManyField('my_app2.Job',blank=False)

class Search(models.Model):
	search = models.CharField(max_length=120,blank=True,null=True)


