from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Task,NewUser
from .forms import TaskForm, NewUserCreationForm

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		form = NewUserCreationForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,'User created successfully!')
			return redirect('login')
		context = {'form':form}
		return render(request,'register.html',context)
		
def loginPage(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			print(username,password)
			user = authenticate(request, username=username,password=password)
			if user is not None:
				login(request,user)
				return redirect('/')
			else:
				messages.info(request, 'Username or Password incorrect')
		context = {}
		return render(request,'login.html',context)
		
def logoutPage(request):
	logout(request)
	return redirect('login')

@login_required(login_url = 'login')
def index(request):
    tasks = Task.objects.all()
    for task in tasks:
    	task.duechecker()
    form = TaskForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {'tasks':tasks,'form':form}
    return render(request,'list.html',context)

@login_required(login_url = 'login')
def updateTask(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance = task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'update_task.html',context)

@login_required(login_url = 'login')
def deleteTask(request,pk):
    item =Task.objects.get(id=pk)
    
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request,'delete.html',context)