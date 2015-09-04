from django.shortcuts import render
from models import Post, UserProfile
from django.contrib.auth.models import User


def index(request):
    return render(request, 'wildlife/index.html', {})


def gallery(request):
    posts = Post.objects.all()
    return render(request, 'wildlife/gallery.html', {'posts': posts})


def user_profile(request, username_slug):
    context_dict = {}
    user_profile = UserProfile.objects.get(slug=username_slug)
    user = user_profile.user
    user_posts = Post.objects.filter(user_profile=user_profile)

    context_dict['profile'] = user_profile
    context_dict['user'] = user
    context_dict['posts'] = user_posts

    return render(request, 'wildlife/profile.html', context_dict)


def post(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    user_profile = post.user_profile
    user = user_profile.user

    return render(request, 'wildlife/post.html', {'user': user, 'profile': user_profile, 'post': post})
