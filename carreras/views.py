from django.shortcuts import render, redirect
from carreras.form import LoginForm, UserCreationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from appcarreras.models import Usuario

def homepage(request):
	return render(request, 'index.html')


def registrar(request):
	message = None
	if request.method == 'POST':
		form_user = UserCreationForm(request.POST or None)
		if form_user.is_valid():
			user = form_user.save()
			usuario = Usuario(user=user)
			usuario.save()
			password = request.POST['password1']
			user_auth = authenticate(username=user.username, password=password)
			login(request, user_auth)
			message = "Te has logueado correctamente"
			return redirect('homepage')	
	else:
		form_user = UserCreationForm(request.POST or None)
	return render(request, "registrar.html", {'form_user':form_user, 'message':message })

def login_page(request):
	message = None
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					message = "Te has logueado correctamente"
					return redirect('lista_carreras')
				else:
					message = "Tu usuario esta inactivo"
			else:
				message = "Nombre de usuario y/o password incorrecto"
	else:
		form = LoginForm()
	return render(request, 'login_page.html', {'message':message,'form':form})

def logout_page(request):
	logout(request)
	return redirect('login_page')


"""
def registrar(request):
	message = None
	if request.method == 'POST':
		form = RegistrarForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			email = request.POST['email']
			user = User.objects.create_user(username, email, password)
			if user is not None:
				user_auth = authenticate(username=username, password=password)
				usuario = Usuario()
				usuario.user = user
				usuario.save()
				if user.is_active:
					login(request, user_auth)
					message = "Te has logueado correctamente"
					return redirect('homepage')
				else:
					message = "Tu usuario esta inactivo"
			else:
				message = "Nombre de usuario y/o password incorrecto"
	else:
		form = RegistrarForm()
	return render(request, 'registrar.html', {'message':message,'form':form})
"""