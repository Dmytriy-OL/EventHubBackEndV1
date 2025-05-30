from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from rest_framework import permissions

from event.views import *
from eventhub import settings

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="API документація",
        default_version="v1",
        description="Опис API викликів",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="hoowhoower@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('event.urls')),
    path('', include('user.urls')),

    # API v1
    path('api/v1/', include([
        path('events/', include(('event.api.urls', 'event'), namespace='events')),
        path('users/', include(('user.api.urls', 'user'), namespace='users')),
        path('swagger/schema/', schema_view.with_ui('swagger'), name='schema-swagger'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ])),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += [path(r"", include("django_storybook.urls"))]

handler404 = pageNotFound
