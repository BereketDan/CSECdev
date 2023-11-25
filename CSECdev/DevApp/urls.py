from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name = 'login'),
    path('login/', views.login, name = 'login'),
    path('member/', views.member, name = 'member'),
    path('feedback/', views.feedback, name = 'feedback'),
]
