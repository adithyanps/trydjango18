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

class Add(models.Model):
	name = models.CharField(max_length=120)
	marks = models.CharField(max_length=120)
	userid =  models.CharField(max_length=120,blank=False)
	def __unicode__(self):
		return self.name
		
class Tweet(models.Model):
	full_name = models.CharField(max_length=120)
	def __unicode__(self):
	 	return self.full_name

class Convert(models.Model):
	status=(('INR',"INR"),
		("USD","USD"),
		("EUR","EUR"),
		("GBP","GBP"),
		("SGB","SGB"),
		("BGN","BGN"),
		("ILS","ILS"),
		("AED","AED"),
		("HKD","HKD"),
		("SGD","SGD"))
	convert_from = models.CharField(choices=status,max_length=3,blank=False,default='INR')
	convert_to = models.CharField(choices=status,max_length=3,blank=False,default='USD')
	amount = models.IntegerField(blank = False)

	def __unicode__(self):
		return self.convert_from

class Reader(models.Model):
	url = models.CharField(max_length=120,blank=False)

class Chat(models.Model):
	message = models.CharField(max_length=120,blank=False)
