from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from entries.views import EntriesHomeView, EntriesView, AddEntryView, EditEntryView, RemoveEntryView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'catalog.views.home', name='home'),
    # url(r'^catalog/', include('catalog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', EntriesHomeView.as_view(), name='home'),
    url(r'^entries/$', EntriesView.as_view(), name='entries'),
    url(r'^entries/add/$', AddEntryView.as_view(), name='add_entry'),
    url(r'^entries/remove/$', RemoveEntryView.as_view(), name='remove_entry'),
    url(r'^entries/edit/$', EditEntryView.as_view(), name='edit_entry'),
)
