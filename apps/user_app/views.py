from django.shortcuts import render, redirect, HttpResponse
import re
from django.contrib import messages
from .models import User, Friend


# Create your views here.
def index(request):
    return render(request, 'user_app/index.html')


def register(request):
    if request.method == "POST":
        server_firstname = request.POST['first_name']
        server_lastname = request.POST['last_name']
        server_email = request.POST['email']
        server_password = request.POST['password']
        try:
            user = User.objects.create(first_name=server_firstname, last_name=server_lastname, email=server_email, password=server_password)
            request.session['id'] = user.id
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            request.session['email'] = user.email
            request.session['password'] = user.password
            return redirect('playlists:home')
        except:
            messages.error(request, 'ERROR: Email already exists!')
            return redirect('users:home')
    else:
        messages.error(request, 'ERROR: Login failed, try again!')
        return redirect('users:home')


def login(request):
    if request.method == "POST":
        server_email = request.POST['email']
        server_password = request.POST['password']
        try:
            user = User.objects.get(email=server_email)
            if user.password == server_password:
                request.session['id'] = user.id
                request.session['first_name'] = user.first_name
                request.session['last_name'] = user.last_name
                request.session['email'] = user.email
                return redirect('playlists:home')
            else:
                messages.error(request, 'ERROR: Incorrect Password!!')
                return redirect('users:home')
        except:
            messages.error(request, 'ERROR: Email not found!')
            return redirect('users:home')
    else:
        messages.error(request, 'ERROR: Login Invalid!')
        return redirect('users:home')


def profile(request):
    return render(request, 'user_app/profile.html')


def edit_profile(request):
    return render(request, 'user_app/edit_profile.html')


def update_profile(request):
    if request.method == "POST":
        server_firstname = request.POST['first_name']
        server_lastname = request.POST['last_name']
        server_password = request.POST['password']
        if server_password == request.POST['confirm_password']:
            try:
                user = User.objects.get(id = request.session['id'])
                user.first_name = server_firstname
                user.last_name = server_lastname
                user.password = server_password
                user.save()
                request.session['first_name'] = user.first_name
                request.session['last_name'] = user.last_name
                request.session['password'] = user.password
                return redirect('users:profile')
            except:
                messages.error(request, 'ERROR: Invalid inputs, try again!')
                return redirect('users:edit_profile')
        else:
            messages.error(request, 'ERROR: Passwords do not match, try again!')
            return redirect('users:edit_profile')
    else:
        messages.error(request, 'ERROR: Invalid inputs, try again!')
        return redirect('users:edit_profile')


def logout(request):
    request.session.clear()
    return redirect('users:home')


def follow_users(request):
    context = {
        "notfriends": User.objects.exclude(id=request.session['id']).exclude(followers__follower_id=request.session['id']),
        "friends": User.objects.filter(followers__follower_id=request.session['id'])
    }
    return render(request, 'user_app/follow_users.html', context)


def follow(request, followee_id):
    Friend.objects.create(follower_id=request.session['id'], followee_id=followee_id)
    return redirect('users:follow_users')


def unfollow(request, followee_id):
    Friend.objects.filter(followee_id=followee_id).delete()
    return redirect('users:follow_users')


def my_followers(request):
    context = {
        "my_followers": User.objects.filter(followers__follower_id=request.session['id'])
        }
    return render(request, 'user_app/my_followers.html', context)


def follower_profile(request, follower_id):
    context = {
        "friend": User.objects.get(id=follower_id)
    }
    return render(request, 'user_app/follower_profile.html', context)
