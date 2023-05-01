from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Post

# Create your views here.


posts = [
    {
        'title': 'Beautiful is better than ugly',
        'author': 'John Doe',
        'content': 'Beautiful is better than ugly',
        'published_at': 'October 1, 2022'
    },
    {
        'title': 'Explicit is better than implicit',
        'author': 'Jane Doe',
        'content': 'Explicit is better than implicit',
        'published_at': 'October 1, 2022'
    }
]


def home(request):
    # return HttpResponse('<h1>Blog Home</h1>')
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'title': "Pythoooonnn"
    }
    return render(request, 'blog/home.html', context)


def about(request):
    # return HttpResponse('<h1>About</h1>')
    return render(request, 'blog/about.html')


@login_required
def create_post(request):
    if request.method == "GET":
        context = {'form': PostForm()}
        return render(request, 'blog/post_form.html', context)
    elif request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'The post has been created successfully.')
            return redirect('posts')
    else:
        messages.error(request, 'Please correct the following errors:')
        return render(request, 'blog/post_form.html', {'form': form})


@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "GET":
        context = {'form': PostForm(instance=post), 'id': id}
        return render(request, 'blog/post_form.html', context)


@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, pk=id)
    context = {'post': post}

    if request.method == 'GET':
        return render(request, 'blog/post_confirm_delete.html', context)
    elif request.method == 'POST':
        post.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('posts')
