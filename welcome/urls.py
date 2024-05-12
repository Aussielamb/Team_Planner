from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('new_member/', views.new_member, name='new_member'),
    path('new_team/', views.new_team, name='new_team'),
    path('view_team/<int:team_id>/', views.view_team, name='view_team'),
    path('update_team/<int:team_id>/', views.team_update, name='update_team'),
    path('member/<int:member_id>/', views.member_details, name='member_details'),
    path('member/update/<int:member_id>/', views.member_update, name='member_update'),
    path('locations/', views.locations, name='locations'),
]
