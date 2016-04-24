from django.conf.urls import patterns, url
from views import hello, current_datetime, hours_ahead, current_datetime_render

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
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
