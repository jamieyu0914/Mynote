from django.urls import path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="API Title",
        default_version='v1',
        description="Your API Description",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', views.IndexView.index, name='index'),
    path('login/', views.ApiLoginView.post, name='api_login'),
    path('create/', views.CreatePostView.post, name='create_post'),
    path('posts/', views.ListPostsView.get, name='list_posts'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]






