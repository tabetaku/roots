from django.urls import path

from apps.domains.home.views import HomeView, HomeApiView

app_name = 'apps.domains.home'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('api/', HomeApiView.as_view(), name='home_api'),
]
