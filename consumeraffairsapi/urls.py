from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'events', views.EventsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^events$', views.events_create),
    url(r'^events/(?P<pk>[0-9]+)$', views.events_detail),
    url(r'^events/series$', views.events_series),
]