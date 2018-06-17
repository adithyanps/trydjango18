# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here0
from .forms import SignUpForm
from .models import SignUp
class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","timestamp","updated"]
	form = SignUpForm
	class Meta:
		model = SignUp


admin.site.register(SignUp, SignUpAdmin)