from . import views
from django.urls import path
from django.contrib.auth import views as log_views



urlpatterns = [
    path("", views.home, name='homepage'),
    path("Blist/<str:id>", views.Blist, name = "blistpage"),
    path('createitem/',views.createItem, name = 'appone_createitem'),
    path("deleteitem/<str:id>/", views.deleteItem, name = "appone_deleteitem"),
    path("register/", views.register, name = "register"),
    path('login/', log_views.LoginView.as_view(template_name='appone/login.html'), name='login'),
    path('logout/', log_views.LogoutView.as_view(template_name='appone/logout.html'), name='logout'),
    path("profile/", views.profile, name = "profile"),
    path('profile/update/', views.profile_update,name='user-profile-update'),

]
