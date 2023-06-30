from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from churras.models import Prato

def cadastro(request):
    #print(f'Method: {request.method}')
    if request.method == 'POST':

        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        senha2 = request.POST['senha2']

        if not nome.strip():
            print('O campo nome não pode ficar em branco')
            return redirect('cadastro')

        if not email.strip():
            print('O campo email não pode ficar em branco')
            return redirect('cadastro')
        
        if senha != senha2 or not senha.strip() or not senha2.strip():
            print('As senhas não coincidem ou está em branco')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            print('E-mail já cadastrado')
            return redirect('cadastro')
        
        if User.objects.filter(username=email).exists():
            print('Usuário já cadastrado')
            return redirect('cadastro')
        
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        #print('Usuário Cadastrado com Sucesso')
        return redirect('login')
    
    return render(request, 'cadastro.html')


def login(request):
    if request.method == 'POST':
        print(f'POST: {request.POST}')

        email = request.POST['email']
        senha = request.POST['senha']

        if email == "" or senha == "":
            print('Os campos e-mail e senha não podem ficar em branco')
            return redirect('login')
        
        print(email, senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)

            if user is not None:
                auth.login(request, user)
                print('Login efetuado com sucesso')

        print('Usuário e/ou senha inválidas')
        return redirect('login')

    return render(request, 'login.html')

def dashboard(request):
    if request.user.is_authenticated:
        pratos = Prato.objects.filter(publicado = True).order_by('-date_prato')

        contexto = {
        'lista_pratos' : pratos
        }

        return render(request, 'dashboard.html', contexto)
    
    return redirect('index')

def logout(request):
    auth.logout(request)
    print('Você realizou o logout!')
    return redirect('index')

def cria_prato(request):
    if request.user.is_authenticated:
        if request.method == 'POST' :   # Recuperar dados do formulário
            print(f'\n{request.POST["nome_prato"]}')

            nome_prato = request.POST['nome_prato']
            ingredientes = request.POST['ingredientes']
            modo_preparo = request.POST['modo_preparo']
            tempo_preparo = request.POST['tempo_preparo']
            rendimento = request.POST['rendimento']
            categoria = request.POST['categoria']
            foto_prato = request.FILES['foto_prato']
            user = get_object_or_404(User, pk=request.user.id)
            prato = Prato.objects.create(
                pessoa=user,
                nome_prato=nome_prato,
                ingredientes=ingredientes,
                modo_preparo=modo_preparo,
                tempo_preparo=tempo_preparo,
                rendimento=rendimento,
                categoria=categoria,
                foto_prato=foto_prato
            )
            prato.save()
            print('Prato criado com sucesso!')
            return redirect('dashboard')


        return render(request, 'cria_prato.html')

    print('Você não tem permissão para Criar Pratos.')
    return redirect('index')