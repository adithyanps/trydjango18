from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from . import views
# from django.contrib import admin
urlpatterns = [

	url(r'^$',views.home,name='home'),
	
	url(r'^contact/$',views.contact,name='contact'),
	url(r'^about/$',views.about,name='about'),
	url(r'^marksheet/$',views.marksheet,name='marksheet'),
	url(r'^add/$',views.add,name='add'),
	url(r'^delete/(?P<pk>\d+)/$', views.delete, name='delete'),
	url(r'^tweets/$',views.tweets,name='tweets'),
	url(r'^currency_converter/$',views.currency_converter,name='currency_converter'),
	url(r'^rss_reader/$',views.rss_reader,name='rss_reader'),
	url(r'^chatroom/$',views.chatroom,name='chatroom'),


	# url(r'^accounts/',include('registration.backends.default.urls')),



]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
