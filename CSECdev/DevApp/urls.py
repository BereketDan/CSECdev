from django.urls import path
from . import views


urlpatterns = [
    path('', views.base, name = 'base'),
    path('login/', views.login, name = 'login'),
    path('index/', views.index, name = 'index'),
    path('feedback/', views.feedback, name = 'feedback'),
]
