from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from ckeditor import urls as ckeditor_urls
from .controls import views as control_view

urlpatterns = patterns('',
    # Examples:
    # url(r'^meeting/', include('meeting.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include(ckeditor_urls)),


    url(r'^$', control_view.Index.as_view(), name='index'),
    url(r'^page/(?P<page>\w+)$', control_view.Pages.as_view(), name='page'),

    url(r'^register$', control_view.RegisterMeeting.as_view(), name='register'),

    url(r'^download$', control_view.DownloadList.as_view(), name='download'),
    url(r'^download/(?P<file_id>\d+)$', control_view.serve_file, name='file'),

)

