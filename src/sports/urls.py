from django.urls import path
from .views import index, teams, new, post, team, sport

urlpatterns = [
    path('', index, name='sports-index'),
    path('teams/', teams, name='teams'),
    path('<slug>/', sport, name='sport-show'),
    path('teams/new', new, name='add-team'),
    path('teams/<slug>', team, name='team'),
    path('posts/<slug>', post, name='post'),
]
