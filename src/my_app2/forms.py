from django import forms
from .models import SignUp
from .models import Job
from .models import Search





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
		if not extension in "com":
			raise forms.ValidationError("please use a valid .com email address")
		return email
	def clean_full_name(self):
		full_name = self.cleaned_data.get("full_name")
		#write validation code
		return full_name
class AddJobForm(forms.ModelForm):
	class Meta:
		model = Job
		exclude = ["job_id"]
class SearchForm(forms.ModelForm):
	class Meta:
		model = Search
		fields =  ["search"]
