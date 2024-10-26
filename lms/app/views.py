from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_page(request):
    return render(request, 'home_page.html')

def admin_login(request):
    if request.method == "POST":
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        if not User.objects.filter(username = username, is_staff=1).exists():
            return redirect('/admin-login/')
        
        user = authenticate(username = username, password = password)

        if user is None:
            return redirect('/admin-login/')
        else:
            login(request, user)
            return redirect('/admin-dashboard/')
    return render(request, 'admin_login.html')

def admin_signup(request):
    if request.method == "POST":
        data = request.POST 
        user = User.objects.create(
            first_name = data.get('first_name'),
            last_name = data.get('last_name'),
            email = data.get('email'),
            is_staff = 1,
            username = data.get('username'),
        )
        user.set_password(data.get('password'))
        user.save()
        return redirect('/admin-login/')
        
    return render(request, 'admin_signup.html')

@login_required(login_url="/admin-login/")
def admin_dashboard(request):
    current_time = datetime.now()
    context = {
        'current_time': current_time,
    }
    return render(request, 'admin_dashboard.html', context)

@login_required(login_url="/admin-login/")
def admin_catalog(request):
    current_time = datetime.now()
    context = {
        'current_time': current_time,
    }
    return render(request, 'admin_catalog.html', context)


@login_required(login_url="/admin-login/")
def admin_books(request):
    current_time = datetime.now()
    context = {
        'current_time': current_time
    }
    return render(request, 'admin_books.html', context)
    
@login_required(login_url="/admin-login/")
def admin_users(request):
    current_time = datetime.now()
    users = User.objects.filter(is_staff=False)
    context = {
        'current_time': current_time,
        'users':users
    }
    return render(request, 'admin_users.html', context)

@login_required(login_url="/admin-login/")
def update_user(request, id):
    data = request.POST
    user = User.objects.get(id = id)
    if request.method == "POST":
        first_name = data.get('first_name')
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')
        user.save()
        return redirect('/admin-users/')
    else:
        context = {'user': user}

    return render(request, 'admin_users.html', context)


def member_login(request):
    if request.method == "POST":
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        if not User.objects.filter(username = username, is_staff=0).exists():
            return redirect('/member-login/')
        
        user = authenticate(username = username, password = password)

        if user is None:
            return redirect('/member-login/')
        else:
            login(request, user)
            return redirect('/member-dashboard/')
        
    return render(request, 'member_login.html')

def member_signup(request):
    if request.method == "POST":
        data = request.POST 
        user = User.objects.create(
            first_name = data.get('first_name'),
            email = data.get('email'),
            is_staff = 0,
            username = data.get('username'),
        )
        user.set_password(data.get('password'))
        user.save()
        return redirect('/member-login/')
    return render(request, 'member_signup.html')

def member_dashboard(request):
    return render(request, 'member_dashboard.html')

def log_out(request):
    logout(request)
    return redirect('/admin-login/')
