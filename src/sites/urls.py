from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from apps.domains.hello_world import urls as hello_world_urls

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('cms/', admin.site.urls),
    path('hello-world/', include(hello_world_urls, namespace='hello_world')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
