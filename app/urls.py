from django.contrib import admin
from django.conf.urls import handler404
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
    path('complete/',views.completing,name='complete'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('add_todo/',views.add_todo,name='add todo'),
    path('add_user/',views.add_user,name='add user'),
    path('verify_user/',views.verify_user,name='verify user'),
    path('edit/<uuid:id>/', views.edit, name='edit_todo'),
    path('delete/<uuid:id>/', views.delete, name='delete_todo'),
    path('mark_complete/<uuid:id>/', views.mark_as_complete, name='mark_as_complete'),
    path('delete_complete/<uuid:id>/', views.delete_completed, name='delete_completed'),
    path('profile/',views.profile,name='profile'),
    path('edit_profile/',views.edit_profile,name='edit profile'),
    path('logout/',views.logout,name='logout'),
]
