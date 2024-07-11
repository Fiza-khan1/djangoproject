from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import UserSignup,postform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from .models import Post
from django.contrib.auth.models import Group
from django.core.cache import cache
def home(request):
     post=Post.objects.all()
     return render(request,'home.html',{'post':post})
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()  
        count = cache.get('count', 0) 
        ip = request.session.get('ip', 0)  
        return render(request, 'dashboard.html', {'posts': posts, 'ip': ip, 'count': count})
    else:
       return HttpResponseRedirect('/')

def user_login(request):
    if request.method=='POST':
        fm=AuthenticationForm(request,request.POST)   
        if fm.is_valid():
          username=fm.cleaned_data['username']
          password=fm.cleaned_data['password']
          user=authenticate(username=username,password=password)
          if user is not None:
             login(request,user)
             messages.success(request,'Login successfully')
             return HttpResponseRedirect(reverse('dashboard'))
    else:
     fm=AuthenticationForm
     print('this one')
    return render(request,'login.html',{'fm':fm})


def user_signup(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=UserSignup(request.POST)
            if fm.is_valid():
                user=fm.save() 
                group=Group.objects.get(name='Author')
                user.groups.add(group)
                messages.success(request,'You have become an author')
                return render(request,'dashboard.html')
        else:
         fm=UserSignup()
        return render(request,'signup.html',{'fm':fm})
    else:
        return render(request,'dashboard.html')
    
def user_logout(request):
   logout(request)
   return HttpResponseRedirect('/login/')

def addpost(request):
   if request.user.is_authenticated:
      if request.method=='POST':
         fm=postform(request.POST) 
         if fm.is_valid():
            fm.save()
            return HttpResponseRedirect(reverse('dashboard')) 
      else:
         fm=postform()
      return render(request,'addPost.html',{'fm':fm})
   else:
      return HttpResponseRedirect('/login/')

def deletePost(request,id):
   if request.user.is_authenticated:
      post=Post.objects.filter(id=id)
      post.delete()
      return HttpResponseRedirect('/dashboard/')
   
   else:
      return HttpResponseRedirect('/')   
def updatePost(request,id):
    if request.user.is_authenticated:
      if request.method=='POST':
         pi=Post.objects.get(pk=id)
         fm=postform(request.POST,instance=pi)  
         if fm.is_valid():
            fm.save()
            return HttpResponseRedirect(reverse('dashboard')) 
      else:
          pi=Post.objects.get(pk=id)
          fm=postform(instance=pi)
      return render(request,'updatepost.html',{'fm':fm})
    else:
      return HttpResponseRedirect('/login/')
