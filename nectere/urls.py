from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework_extensions.routers import ExtendedSimpleRouter
from app.views import *

router = ExtendedSimpleRouter()

users_routes = router.register(
    r'user',
    UserViewSet,
    base_name='user'
)
users_routes.register(
    r'filter-profile',
    UserFilterDataViewSet,
    base_name='user-filter-profile',
    parents_query_lookups=['user']
)
users_routes.register(
    r'filter-options',
    MFilterOptionsViewSet,
    base_name='user-filter-options',
    parents_query_lookups=['user']
)

filter_route = router.register(
    r'filter',
    MFilterViewSet,
    base_name='filter',
)
filter_route.register(
    r'options',
    MFilterOptionsViewSet,
    base_name='filter-options',
    parents_query_lookups=['matching_function']
)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)