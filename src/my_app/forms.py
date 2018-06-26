from django import forms
from .models import SignUp
from .models import Add
from .models import Tweet

class TweetForm(forms.ModelForm):
	class Meta:
		model = Tweet
		fields = ["full_name"]
	def clean_full_name(self):
		full_name = self.cleaned_data.get("full_name")
		return full_name

class AddForm(forms.ModelForm):
	class Meta:
		model = Add
		fields = ["name","marks"]
	def clean_name(self):
		name = self.cleaned_data.get("name")
		return name
	def clean_marks(self):
		marks = self.cleaned_data.get("marks")
		return marks
	
		

class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()


	def clean_email(self):
		email = self.cleaned_data.get("email")
		email_base, provider = email.split("@")
		domain, extension = provider.split(".")
		#if not domain == "USC":
		#	raise forms.ValidationError("please make sure you use your USC email.")
		if not extension in "edu":
			raise forms.ValidationError("please use a valid .EDU email address")
		return email


class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ["full_name","email"]
	def clean_email(self):
		email = self.cleaned_data.get("email")
		email_base, provider = email.split("@")
		domain, extension = provider.split(".")
		# if not domain == "USC":
		# 	raise forms.ValidationError("please make sure you use your USC email.")
		if not extension in "edu":
			raise forms.ValidationError("please use a valid .EDU email address")
		return email
	def clean_full_name(self):
		full_name = self.cleaned_data.get("full_name")
		#write validation code
		return full_name
