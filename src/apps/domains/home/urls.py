from django.urls import path

from apps.domains.home.views import HomeView

app_name = 'apps.domains.home'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
