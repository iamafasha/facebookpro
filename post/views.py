from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView
from user.forms import LoginForm
from django.utils import timezone
from .models import Post, PostImage
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
    context ={
        'post':"hello"
    }
    return render(request, 'post/single_post.html',context)