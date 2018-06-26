# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import ContactForm
from .forms import SignUpForm
from .forms import AddForm
from .forms import TweetForm
from .models import SignUp 
from .models import Add
from .models import Tweet

import requests
import json 
from requests_oauthlib import OAuth1

# Create your views here.
def home(request):
	title = "SignUp Now"
	form = SignUpForm(request.POST or None)

	context = { "title":title,"form": form	}


	if form.is_valid():
		#form.save()
		#print request.POST['email']
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "new full_name"
		instance.full_name = full_name
		#if not instance.full_name:
		#	instance.full_name = "justin"
		instance.save()
		context = {"title":"thank you"}

	if request.user.is_authenticated() and request.user.is_staff:
		# print(SignUp.objects.all())
		# i = 1
		# for instance in SignUp.objects.all():
		# 	print(i)
		# 	print(instance)
		# 	i += 1
		queryset = SignUp.objects.all().order_by('-timestamp')
		context = {"queryset":queryset}
	return render(request,'home.html',context)

def contact(request):
	title = "Contact Us"
	title_align_center = True

	form = ContactForm(request.POST or None)
	if form.is_valid():
		#for key,value in form.cleaned_data.iteritems():
			#print key,value 
			#print form.cleaned_data.get(key)
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		#print email,message,full_name
		subject = "site contact form"
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email,"youotheremail@email.com"]
		contact_message ="%s: %s via %s"%(
			form_full_name,
			form_message,
			form_email)
		some_html_message = """
		<h1>helloo</h1>
		"""
		send_mail(subject,
			contact_message,
			from_email,
			to_email,
			html_message = some_html_message,
			fail_silently=True)

	context = { "form": form,
	"title":title,
	"title_align_center":title_align_center, }
	
	return render(request, "forms.html",context)

def about(request):
	return render(request,'about.html',{})

def marksheet(request):
	form=Add.objects.all()
	# print(Add.objects.all())
	#if request.user.is_authenticated():
	# print(request)
	
	context={"form":form}

	return render(request,"marksheet.html",context)
def add(request):
	message = "welcome"
 	form = AddForm(request.POST or None)
 	context = { "message":message,"form":form }
 	if form.is_valid():
 		instance = form.save(commit=False)
 		form.cleaned_data["userid"] = request.user.id 
 		if instance.name:
 			instance.userid = request.user.id
 			instance.save()
 			context = {"message":"thankyou"}

 	return render(request,'add.html',context)


def delete(request,pk):
	query = Add.objects.get(id=pk)
	query1 = query.userid
	try:
		if int(request.user.id) == int(query1):
			Add.objects.filter(id=pk).delete()
		context = {"title":"OOPS! ENTRY DELETED"}
	except:
		context={"title":"cannot delete"}
	return render(request,'delete.html',context)


def tweets(request):
	message = "Get-Tweets"
	form = TweetForm(request.POST or None)
	context = { "message":message,"form":form }
	if form.is_valid():
		instance = form.save(commit=False)
		username = form.cleaned_data["full_name"]
		Consumer_Key='afcB58TdOAfsBgaiTzdYbzvPL'
		Consumer_Secret='I0CAM68ikunSSd99cX8X5r6CaZEC08GNKEzp1EkCjI6kc2xArS'
		Access_Token ='1011198782065635329-tqi6WW2GIn0u9m1qevJ7o0TZaGikaw'
		Access_Token_Secret ='Q2BeZZEhH57jzBIATOwjHmzUr3cTvjTdcyFSTXH8mmqvW'
		# username=raw_input("enter the username:")
		url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+username+"&tweet_mode=extended&count=100"
		auth = OAuth1(Consumer_Key,Consumer_Secret,Access_Token, Access_Token_Secret)
		r=requests.get(url,auth=auth)
		dic=r.json()
		instance.save()
		#print dict
		value=[]
		for item in dic:
			value.append(item["full_text"])

			context = { "value":value }


	return render(request,'tweet/tweets.html',context)