from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

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


def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

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
            last_name = data.get('last_name'),
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

