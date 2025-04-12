from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login,logout

def register_view(request):
    if request.method == 'POST':  # Se o usuário estiver enviando o formulário
        user_form = UserCreationForm(request.POST)  # Criamos um formulário com os dados enviados
        if user_form.is_valid():  # Validamos para ver se está tudo correto
            user_form.save()  # Salvamos o usuário no banco de dados
            return redirect('login')  # Redirecionamos para a lista de carros
    else:  # Caso a requisição não seja POST, ou algo dê errado
        user_form = UserCreationForm()  # Criamos um formulário vazio para o usuário preencher

    return render(request, 'register.html', {'user_form': user_form})
    # Renderizamos a página com o formulário

def login_view(request):
    if request.method == 'POST': #coletando o que o usuário enviou no formulário
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password) #autenticando no bd para ver se o usuário existe
        if user is not None:
            login(request, user)
            return redirect('cars_list')
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()
    return render(request,'login.html',{'login_form': login_form})

def logout_view(request):
    logout(request)
    return redirect('cars_list')
