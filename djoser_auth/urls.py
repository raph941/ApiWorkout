from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

# for swagger and redoc
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Welcome To the Api",
      default_version='v1',
      description="Demo Api",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="raph941@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    url(r'^auth/', include('djoser.urls')),
    # url(r'^auth/', include('djoser.urls.jwt')),
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^articles/', include('articles.urls')),
    path('admin/', admin.site.urls),

    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]