from django.shortcuts import render, redirect
from carreras.form import LoginForm
from django.contrib.auth import authenticate, login, logout

def homepage(request):
	return render(request, 'index.html')

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
