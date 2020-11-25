from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth import authenticate ,logout as signout ,login
from .models import User 
from django.contrib import messages
from .forms import LoginForm , RegisterForm , ProfileForm
from post.views import index as home
# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        login_form=LoginForm()
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(request,username=username, password=password)
                if user is not None:
                    login(request, user)
                    return home(request)        
                else:
                    messages.add_message(request, messages.ERROR,'Wrong username or password')
        context = {"form": login_form}
        return render(request, 'user/signin.html',context)
    else:
        return home(request)
    
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    register_form=RegisterForm()
    if request.method == 'POST':
        register_form=RegisterForm(request.POST)
        if register_form.is_valid():
            first_name = register_form.cleaned_data.get('first_name')
            last_name = register_form.cleaned_data.get('last_name')
            user_name = register_form.cleaned_data.get('user_name')
            email = register_form.cleaned_data.get('email')
            password = register_form.cleaned_data.get('password')
            password_again = register_form.cleaned_data.get('password_again')
            try:
                user= User.objects.get(username=user_name)
            except User.DoesNotExist:
                if password == password_again:
                    user= User.objects.create_user(user_name, password= password, email=email ,first_name=first_name, last_name=last_name)
                    user.save()
                    login(request,user)
                    return redirect('home')

    context = {"form": register_form}
    return render(request, 'user/register.html',context)

def settings(request):
    if request.user.is_authenticated:
        print(request.user.first_name)
        intial_data = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'user_name': request.user.username,
            'email':request.user.email,
            'bio':request.user.bio
            }
        profile_form=ProfileForm(intial_data)
        if request.method == "POST":
            profile_form=ProfileForm(request.POST, request.FILES)
            if profile_form.is_valid():
                user_name = profile_form.cleaned_data.get('user_name')
                profile_picture = profile_form.cleaned_data.get('profile_picture')
                print(profile_picture)
                bio = profile_form.cleaned_data.get('bio')
                new_user= User.objects.get(pk=request.user.id)
                if new_user is not None:
                    new_user.profile_picture=profile_picture,
                    new_user.bio=bio
                    new_user.save()

        context ={
            "profile_form":profile_form
        }
        return render(request, 'user/settings.html',context)
    return redirect('home')

def logout(request):
    signout(request)
    return redirect('home')