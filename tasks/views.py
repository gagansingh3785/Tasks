from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from user.models import NewUser
from .models import Task, Notifications


def user_login(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('home'))
	if request.method == "POST":
		print(request.POST['email'])
		print(request.POST['password'])
		user = authenticate(password=request.POST['password'], email=request.POST['email'])
		print(user)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse('home'))

	return render(request, 'tasks/login.html', {})

@login_required(login_url="login")
def home(request):
	pending_tasks = Task.objects.filter(status="P")
	completed_tasks = Task.objects.filter(status="C")
	notifications = Notifications.objects.filter(user=request.user, read=False)
	print(completed_tasks)
	return render(request, 'tasks/home.html', {"pending_tasks": pending_tasks, "completed_tasks": completed_tasks, "notifications": notifications})


@login_required(login_url="login")
def navbar(request):
	return render(request, 'tasks/navbar.html', {})


@login_required(login_url="login")
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('login'))


def register(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('home'))
	if request.method == "POST":
		print(request.POST['email'])
		print(request.POST['password'])
		user = NewUser()
		user.email = request.POST['email']
		user.set_password(request.POST['password'])
		user.user_type = request.POST['user_type']
		user.save()
		return HttpResponseRedirect(reverse('login'))
	return render(request, 'tasks/register.html', {})


@login_required(login_url="login")
def create(request):
	if request.method == "POST":
		task = Task()
		task.name = request.POST["name"]
		task.description = request.POST["description"]
		task.creator = request.user
		moderator = NewUser.objects.get(email="gs35@iitbbs.ac.in")
		task.moderator = moderator
		task.status = 'P'
		task.save()
		notification = Notifications()
		notification.user = moderator
		notification.title = request.user.email + " created a new task: " + task.name
		notification.read = False
		notification.save()
		return HttpResponseRedirect(reverse('home'))
	return render(request, 'tasks/create.html', {})


@login_required(login_url="login")
def completed(request, id):
	task = Task.objects.get(id=id)
	print(task)
	task.status = 'C'
	task.save()
	notification = Notifications()
	notification.user = task.creator
	notification.title = request.user.email + " completed a task: " + task.name
	notification.read = False
	notification.save()
	return HttpResponse("completed")

@login_required(login_url="login")
def read(request, id):
	notification = Notifications.objects.get(id=id)
	notification.read = True
	notification.save()
	return HttpResponse("read")