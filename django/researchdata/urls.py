from django.urls import path
from . import views, apps

app_name = apps.app_name

urlpatterns = [
    path('', views.SurveyCreateView.as_view(), name='survey-create'),
    path('survey/<slug:slug>/', views.SurveyUpdateView.as_view(), name='survey-update'),
    path('thanks/<slug:slug>/', views.SurveyFinalUpdateView.as_view(), name='survey-final'),
]
