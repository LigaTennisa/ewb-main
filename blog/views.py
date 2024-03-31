
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm


@login_required
def delete_post(request, id):
    queryset = Post.objects.filter(author=request.user)
    post = get_object_or_404(queryset, pk=id)
    context = {'post': post}

    if request.method == 'GET':
        return render(request, 'blog/post_confirm_delete.html', context)
    elif request.method == 'POST':
        post.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('posts')


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('find_partner')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


@login_required
def find_partner(request):
    posts = Post.objects.filter(author=request.user)  # Получаем посты автора
    context = {'posts': posts}
    return render(request, 'blog/find_partner.html', context)


@login_required
def edit_post(request, id):
    queryset = Post.objects.filter(author=request.user)
    post = get_object_or_404(queryset, pk=id)

    if request.method == 'GET':
        context = {'form': PostForm(instance=post), 'id': id}
        return render(request, 'blog/post_form.html', context)

    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'The post has been updated successfully.')
            return redirect('posts')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'blog/post_form.html', {'form': form})


def home(request):

    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')


def tournaments(request):
    return render(request, 'blog/tournaments.html')


def courts(request):
    return render(request, 'blog/courts.html')


def training(request):
    return render(request, 'blog/training.html')


def contact(request):
    return render(request, "blog/contact.html")


def aboutus(request):
    return render(request, "blog/aboutus.html")


def myprofile(request):
    return render(request, "blog/myprofile.html")


def find_partner(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, "blog/find_partner.html", context)


# views.py


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            # Перенаправляем
            return redirect('find_partner')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})


@login_required
def respond_to_post(request, id):
    post = get_object_or_404(Post, pk=id)
    # Здесь вы можете выполнить дополнительные действия, например, отправить уведомление автору поста о том, что кто-то откликнулся на его форму.
    return HttpResponse("Откликнулись на пост {}".format(post.title))


@login_required
def my_profile(request):
    user = request.user
    posts = Post.objects.filter(author=user)

    context = {
        'user': user,
        'posts': posts,
    }

    return render(request, 'myprofile.html', context)
