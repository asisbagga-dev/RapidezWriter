from django.urls import path, include
from . import views

app_name = 'resumeAnalysis'

urlpatterns = [
    path('', views.resume_upload, name='uploadresume'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('test/', views.test, name='test'),
]
