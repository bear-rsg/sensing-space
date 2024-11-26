from django.urls import path
from . import views, apps

app_name = apps.app_name

urlpatterns = [
    path('about/', views.AboutTemplateView.as_view(), name='about'),
    path('campus/', views.CampusTemplateView.as_view(), name='campus'),
    path('cookies/', views.CookiesTemplateView.as_view(), name='cookies'),
]
