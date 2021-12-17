from django.shortcuts import render
from user.models import Post
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {'posts': posts}
    return render(request, 'home/index.html', context)