from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from rest_framework.permissions import AllowAny

from event.views import *
from eventhub import settings


schema_view = swagger_get_schema_view(
    openapi.Info(
        title="API документація",
        default_version="v1",
        description="Опис API викликів",
    ),
    public=True,
    permission_classes=(AllowAny,),
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
    ])),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound
