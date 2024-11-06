"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views import CreateUserGroupsViewSets, PermissionsViewSet


# Create a router and register the viewset
router = DefaultRouter()
router.register(r'usergroups', CreateUserGroupsViewSets)


# Manually define the URL patterns for the viewset

permissions_list = PermissionsViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
permissions_detail = PermissionsViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

usergroups_list = CreateUserGroupsViewSets.as_view({
    'get': 'list',
    'post': 'create'
})
usergroups_detail = CreateUserGroupsViewSets.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs'),
    path('api/user/', include('user.urls')),
   #path('api/', include(router.urls)),  # Include the router's URLs
    path('api/core/usergroups/', usergroups_list, name='usergroups-list'),
    path('api/core/usergroups/<int:pk>/', usergroups_detail, name='usergroups-detail'),
     path('api/core/permissions/', permissions_list, name='permissions-list'),
    path('api/core/permissions/<int:pk>/', permissions_detail, name='permissions-detail'),
]
