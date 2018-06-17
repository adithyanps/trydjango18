from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from . import views
# from django.contrib import admin
urlpatterns = [

	url(r'^$',views.home,name='home'),
	
	url(r'^contact/$',views.contact,name='contact'),
	url(r'^about/$',views.about,name='about'),
	url(r'^accounts/',include('registration.backends.default.urls')),



]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
