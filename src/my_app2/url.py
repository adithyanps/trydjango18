from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from . import views
# from django.contrib import admin
urlpatterns = [
	url(r'^$',views.home,name='home'),
	url(r'^add_job/$',views.add_job,name='add_job'),
	url(r'^applied_jobs/$',views.applied_jobs,name='applied_jobs'),
	url(r'^view_jobs/$',views.view_jobs,name='view_jobs'),
	url(r'^apply/(?P<pk>\d+)/$',views.apply,name='apply'),
	url(r'^delete/(?P<pk>\d+)/$',views.delete,name='delete'),
	url(r'^search/$',views.search,name='search'),





]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
