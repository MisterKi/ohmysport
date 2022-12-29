from django.shortcuts import render
from django.apps import apps as django_apps


def index(request):
    post_model = django_apps.get_model('sports', 'Post')
    sport_model = django_apps.get_model('sports', 'Sport')
    team_model = django_apps.get_model('sports', 'Team')

    last_post = post_model.objects.last()
    posts = post_model.objects.all().order_by('-id')[1:5]
    sport = sport_model.objects.get(pk=last_post.teams.last().sport_id)
    teams = team_model.objects.all().order_by('-id')[:4]

    contexts = {
        'last_post': last_post,
        'sport': sport,
        'teams': teams,
        'posts': posts,
    }

    return render(request, 'ohmysport/index.html', context=contexts)
