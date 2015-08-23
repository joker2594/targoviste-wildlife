from django.shortcuts import render
from models import Post, UserProfile
from django.contrib.auth.models import User


def index(request):
    posts = Post.objects.all()
    return render(request, 'wildlife/index.html', {'posts': posts})


def user_profile(request, username_slug):
    context_dict = {}
    user_profile = UserProfile.objects.get(slug=username_slug)
    user = user_profile.user
    user_posts = Post.objects.filter(user=user)

    context_dict['profile'] = user_profile
    context_dict['user'] = user
    context_dict['posts'] = user_posts

    return render(request, 'wildlife/profile.html', context_dict)

