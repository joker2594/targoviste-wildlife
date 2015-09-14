from django.shortcuts import render, HttpResponseRedirect
from models import Post, UserProfile
from forms import PostForm
from django.contrib.auth.models import User


def index(request):
    context = {}
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        context['profile'] = user_profile

    return render(request, 'wildlife/index.html', context)


def gallery(request):
    context = {}
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        context['profile'] = user_profile
    posts = Post.objects.all().order_by('-date_added')
    context['posts'] = posts
    return render(request, 'wildlife/gallery.html', context)


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


def add_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            user_profile = UserProfile.objects.get(user=request.user)
            post = post_form.save(commit=False)
            post.user_profile = user_profile

            if 'picture' in request.FILES:
                post.picture = request.FILES['picture']

            post.save()

            return HttpResponseRedirect('/gallery/')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print post_form.errors

    else:
        post_form = PostForm()

    return render(request, 'wildlife/add_post.html', {'post_form': post_form})
