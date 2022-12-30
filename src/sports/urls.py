from django.urls import path
from .views import index, teams, newteam, post, team, sport, newpost

urlpatterns = [
    path('', index, name='sports-index'),

    path('teams/', teams, name='teams'),
    path('teams/<slug>/', team, name='team'),
    path('teams/new/', newteam, name='add-team'),

    path('<slug>/', sport, name='sport-show'),

    path('posts/<slug>/', post, name='post'),
    path('posts/new/', newpost, name='newpost'),
]
