from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from contactlist.views import ContactViewSet, api_root, ContactView


# contactlist
contact_list = ContactViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
# contact-details
contact_detail = ContactViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

# API endpoints
urlpatterns = format_suffix_patterns([
	url(r'^$', views.ContactView, name='ContactView'),
    url(r'^$', api_root),
    url(r'^contactlist/$', contact_list, name='contact-list'),
    url(r'^contactlist/(?P<pk>[0-9]+)/$', contact_detail, name='contact-detail'),
])
