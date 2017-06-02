from django.conf.urls import url, include
from django.contrib import admin
from contactlist import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')
# registering the views with router
router = DefaultRouter()
router.register(r'contactlist', views.ContactViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('contactlist.urls', namespace='contactlist')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^schema/$', schema_view),
]
