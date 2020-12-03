from django.shortcuts import render, redirect
from django.views.generic.edit import FormView, CreateView
from user.forms import LoginForm
from django.utils import timezone
from .models import Post, Comment, PostLike, PostImage
from user.models import User


# Create your views here.
def index(request):
    login_form=LoginForm()
    posts=Post.objects.filter(approved=True).order_by('-published_date')
    context = {
        "form": login_form,
        "posts":posts,
        }
    return render(request, 'post/home.html',context )

# Create your views here.
def profile(request ,username=None):
    login_form=LoginForm()
    posts=Post.objects.filter(approved=True ).order_by('-published_date')
    error = []
    try:
        user=User.objects.get(username=username)
        posts=Post.objects.filter(author=user, approved=True , ).order_by('-published_date')
    except User.DoesNotExist:
        error= {
            "message":"account never exists"
        }
        posts = {}
    context = {
        "form": login_form,
        "posts":posts,
        "error":error,
        "username":username
    }
    return render(request, 'post/timeline.html',context)

def single_post(request, username, id):
    username=User.objects.get(username=username)
    post= Post.objects.get(author = username.id, pk=id)
    context ={
        'post':post
    }
    return render(request, 'post/single_post.html',context)

def create_post(request,username):
    if(request.method=="POST"):
        text = request.POST.get('description')
        post =Post(author=request.user,text=text)
        post.save()
        images=request.FILES.getlist('upload')
        for image in images:
            post_image=PostImage(post=post,image=image,caption="")
            post_image.save()
        return redirect('sinlge_post', username=request.user.username, id =post.id )

def comment(request, username, post_id , comment_id):
    username = User.objects.get(username=username)
    comment = Comment.objects.get(id =comment_id)
    if request.method == 'GET':
        setapprove=request.GET.get('set_approve')
        if(setapprove == "true"):
            comment.approved=True
            comment.save()
    return redirect('sinlge_post', username= username,id =post_id )

def create_comment(request,username,post_id):
    if request.method == 'POST' and request.user.is_authenticated:
        comment_text=request.POST.get('post_comment')
        try:
            Comment.objects.create(author=request.user,reply_to=Post.objects.get(id=post_id),text=comment_text,approved=False)
        except User.DoesNotExist:
            pass
        return redirect('sinlge_post', username= username,id =post_id )
    elif request.method == 'GET':
        return redirect(request.META.get('HTTP_REFERER'))

def post_like(request,username,post_id):
    if request.method == 'GET':
        action=request.GET.get('action').strip()
        post = Post.objects.get(id=post_id)
        if action=='like' :
            try:
                PostLike.objects.get(author=request.user,post=post)
            except PostLike.DoesNotExist:
                print("")
                PostLike.objects.create(author=request.user,post=post).save()
        elif action=='unlike':
            PostLike.objects.get(author=request.user,post=post).delete()
    return redirect(request.META.get('HTTP_REFERER'))