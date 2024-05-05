from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('new_member/', views.new_member, name='new_member'),
    path('new_team/', views.new_team, name='new_team'),
    path('member/<int:member_id>/', views.member_details, name='member_details'),
]
