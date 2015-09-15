from django.conf.urls import patterns, url

# Create your tests here.
urlpatterns = patterns('',
	url(r'^login$', 'accounts.views.login', name='login'),
	url(r'^logout$', 'accounts.views.logout', name='logout'),
)	