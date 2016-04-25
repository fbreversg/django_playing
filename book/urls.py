from django.conf.urls import patterns, url, include
from django.contrib import admin
from views import hello, current_datetime, hours_ahead, current_datetime_render

admin.autodiscover()

urlpatterns = patterns('',
                       (r'^admin/', include(admin.site.urls)),
                       url(r'^hello/$', hello),
                       url(r'^time/plus/(\d{1,2})/$', hours_ahead),
                       url(r'^time/$', current_datetime),
                       url(r'^timeRender/$', current_datetime_render),
                       url(r'^$', hello),

                       # Examples:
                       # url(r'^$', 'book.views.home', name='home'),
                       # url(r'^book/', include('book.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       # url(r'^admin/', include(admin.site.urls)),
                       )
