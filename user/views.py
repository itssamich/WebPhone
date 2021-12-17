from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, postCreationForm
from django.core.paginator import Paginator
from user.models import Post, User

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home:index')
    else:
        form = RegistrationForm()
    return render(request, 'user/register.html', {'form': form})

def profile(request, username):
    current_user = User.objects.get(pk=username)

    posts = Post.objects.filter(author=current_user)
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)


    return render(request, 'user/profile.html', {'user': current_user, 'posts':posts})

def createPost(request, username):
    if request.method == 'POST':
        form = postCreationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            post.save()

            return redirect('home:index')
    else:
        form = postCreationForm()
    return render(request, 'posts/createPost.html', {'form': form})