from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from apps.domains.home import urls as home_urls

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('cms/', admin.site.urls),
    path('/', include(home_urls, namespace='home')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
