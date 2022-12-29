from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Team, Post, Sport
from .forms import TeamForm, PostForm


def index(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'sports/index.html', context={'posts': posts})


# Sports
def sport(request, slug):
    posts = []
    sport = Sport.objects.get(slug=slug)
    for team in sport.team_set.all():
        for post in team.post_set.all():
            if not post in posts:
                posts.append(post)
    return render(request, 'sports/sports/sport.html', context={'sport': sport, 'posts': posts})


# Teams
def teams(request):
    teams = Team.objects.all()
    return render(request, 'sports/teams/teams.html', context={'teams': teams})


def newteam(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    else:
        form = TeamForm()
        return render(request, 'sports/teams/new.html', context={'form': form})


def team(request, slug):
    team = Team.objects.get(slug=slug)
    return render(request, 'sports/teams/team.html', context={'team': team})


# Posts
def newpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    else:
        form = PostForm()
        return render(request, 'sports/posts/new.html', context={'form': form})


def post(request, slug):
    post = Post.objects.get(slug=slug)
    sport = Sport.objects.get(pk=post.teams.last().sport_id)
    return render(request, 'sports/posts/post.html', context={'post': post, 'sport': sport})
