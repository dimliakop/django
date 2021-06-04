from django.conf.urls import include, url
from django.urls import path
from rest_framework.routers import DefaultRouter, BaseRouter
from versioning import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
# router.register(r'documents', views.DocumentViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'revisions', views.RevisionViewSet)


# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    path('documents/<path:url>/', views.DocumentViewSet.as_view({'get': 'retrieve'})),
    url(r'^documents/$', views.DocumentViewSet.as_view({'get': 'list', 'post': 'perform_create', 'put': 'update'})),
]


