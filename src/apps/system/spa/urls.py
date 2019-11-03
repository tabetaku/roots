from django.urls import path

from apps.system.spa.views import SpaView

app_name = 'apps.system.spa'
urlpatterns = [
    path('', SpaView.as_view(), name='spa'),
]
