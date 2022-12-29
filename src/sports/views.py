from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Team, Post, Sport
from .forms import TeamForm


def index(request):
    posts = Post.objects.all()
    return render(request, 'sports/index.html', context={'posts': posts})


def sport(request, slug):
    posts = []
    sport = Sport.objects.get(slug=slug)
    for team in sport.team_set.all():
        for post in team.post_set.all():
            if not post in posts:
                posts.append(post)
    return render(request, 'sports/sport.html', context={'sport': sport, 'posts': posts})


def teams(request):
    teams = Team.objects.all()
    return render(request, 'sports/teams/teams.html', context={'teams': teams})


def team(request, slug):
    team = Team.objects.get(slug=slug)
    return render(request, 'sports/teams/team.html', context={'team': team})


def post(request, slug):
    post = Post.objects.get(slug=slug)
    sport = Sport.objects.get(pk=post.teams.last().sport_id)
    return render(request, 'sports/post.html', context={'post': post, 'sport': sport})


def new(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    else:
        form = TeamForm()
        return render(request, 'sports/teams/new.html', context={'form': form})
