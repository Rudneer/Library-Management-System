"""
URL configuration for lms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-dashboard/', admin_dashboard, name = 'admin_dashboard'),
    path('', home_page, name = 'home_page'),
    path('logout/', log_out, name = 'logout'),
    path('admin-login/', admin_login, name = 'admin-login'),
    path('admin-catalog/', admin_catalog, name = 'admin-catalog'),
    path('admin-books/', admin_books, name = 'admin-books'),
    path('admin-users/', admin_users, name = 'admin-users'),
    path('update-user/<id>/', update_user, name = 'update-user'),
    path('admin-signup/', admin_signup, name = 'admin-login'),
    path('member-login/', member_login, name = 'member-login'),
    path('member-signup/', member_signup, name = 'member-signup'),
    path('member-dashboard/', member_dashboard, name = 'member-dashboard'),

]
