from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
	url(r'^login$', 'accounts.views.persona_login', name='persona_login'),
	url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
