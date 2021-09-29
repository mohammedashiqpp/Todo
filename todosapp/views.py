from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView

from .forms import frm
from todosapp.models import *


def home(request):
  obj1 = post.objects.all()
  if request.method=='POST':
    posts=request.POST['tasks']
    date=request.POST['date']
    obj=post.objects.create(post=posts,date=date)
    obj.save()
  return render(request,'home.html',{'obj1':obj1})

class generic(ListView):
    model = post
    template_name = 'home.html'
    context_object_name = 'obj1'
def reg(request):

  if request.method == 'POST':
    username = request.POST['username']
    password1 = request.POST['psw']
    password2 = request.POST['psw-repeat']
    if password1 == password2:
      if User.objects.filter(username=username).exists():
        messages.info(request, 'already ready taken')
        return request('reg')
      else:
        user = User.objects.create_user(username=username, password=password1)
        user.save();
        return redirect('/')
    else:
      messages.info(request,'password does not mach')
      return redirect('/')

  else:

   return render(request,'home.html')

def log(reqeust):
    if reqeust.method == 'POST':
      username = reqeust.POST['username']
      password = reqeust.POST['password']
      user = auth.authenticate(username=username, password=password)
      if user is not None:
        auth.login(reqeust, user)
        return redirect('/')
      else:
        messages.info(reqeust, 'invalid username or password')
        return redirect('log')

    else:
      return render(reqeust, 'home.html')


def logg(reqeust):
  auth.logout(reqeust)
  return redirect('/')

def deli(request,taskid):
    tasks=post.objects.get(id=taskid)
    if request.method=="POST":
        tasks.delete()
        return redirect('/')
    return render(request,'delete.html',{'tasks':tasks})
def update(request,id):
    tasks=post.objects.get(id=id)
    form=frm(request.POST or None,instance=tasks)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'tasks':tasks,'form':form})