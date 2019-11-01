from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from apps.domains.home import urls as home_urls
from libs.django.swagger.custom_schema_view import CustomSchemaView

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('cms/', admin.site.urls),
    path('', include(home_urls, namespace='home')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
        path('docs/swagger/', CustomSchemaView.with_ui(), name='schemas-swagger-ui'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
