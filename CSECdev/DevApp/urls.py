from django.urls import path
from . import views 




urlpatterns = [
    path('', views.login, name = 'login'),
    path('login/', views.login, name = 'login'),
    path('member/', views.member, name = 'member'),
    path('feedback/', views.feedback, name = 'feedback'),
    path('event/', views.event, name = 'event'),
    path('dashboard/', views.dashboard, name = "dashboard"),
    path('settings/', views.settings, name = "settings"),
    path('logout/', views.logout, name = "logout"),
    # path('?editUser/', views.editUser, name = "editUser"),
    path('member/deleteMember/<int:id>/', views.deleteMember, name = "deleteMember"),
    path('member/updateMember/<int:id>/', views.updateMember, name = "updateMember"),
     path('update/updateMemberRecord/<int:id>', views.updateMemberRecord, name='updateMemberRecord')
]
