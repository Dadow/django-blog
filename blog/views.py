from django.shortcuts import render
from .forms import PostForm
from .models import Post
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone

#from django.contrib.auth.models import User
#from html import unescape

# Create your views here.
def post_list(request):
    '''
    PostVars = []
    # Otra forma de hacerlo
    for post in Post.objects.all():
        PostVars.append(
            {
             'titulo':post.title,
             'texto':unescape(post.text),
             'autor':User.objects.get(id=post.author_id).username
            }
        )
    '''
    Pooost = Post.objects.all()
    return render(request, 'blog/post_list.html', {'PostVars':Pooost})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:   
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_delete(request, pk):
    Post.objects.filter(pk=pk).delete()
    return redirect('/')