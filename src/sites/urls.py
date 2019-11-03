from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

from apps.domains.home import urls as home_urls
from apps.system.spa import urls as spa_urls
from libs.django.swagger.custom_schema_view import CustomSchemaView

urlpatterns = [
    path('docs/swagger/', CustomSchemaView.with_ui(), name='schemas-swagger-ui'),

    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('cms/', admin.site.urls),
    path('home/', include(home_urls, namespace='home')),

    # 위에 정의된 URL 이외의 모든 경로는 SPA 로 넘긴다.
    re_path(r'^.*$', include(spa_urls, namespace='spa')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
