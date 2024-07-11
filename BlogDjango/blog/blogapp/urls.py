
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name="contact"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('signup/',views.user_signup,name="signup"),
    path('addpost/',views.addpost,name='addpost'),
    path('updatepost/<int:id>/', views.updatePost, name='updatepost'),
    path('deletePost/<int:id>/', views.deletePost, name='deletepost'),
]
