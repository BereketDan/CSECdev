from django.urls import path
from . import views


urlpatterns = [
    path('', views.base, name = 'base'),
    path('login/', views.login, name = 'login'),
    path('member/', views.member, name = 'member'),
    path('feedback/', views.feedback, name = 'feedback'),
]
