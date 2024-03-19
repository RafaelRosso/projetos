from django.shortcuts import render


def index(request):
    titulo = 'Home'
    return render(request,'app_site/index.html', {'titulo': titulo})

def db1(request):
    titulo = 'Dasboard 1'
    return render(request,'app_site/dashboard1.html', {'titulo': titulo})

def db2(request):
    titulo = 'Dasboard 2'
    return render(request,'app_site/dashboard2.html', {'titulo': titulo})

def db3(request):
    titulo = 'Dasboard 3'
    return render(request,'app_site/dashboard3.html', {'titulo': titulo})

def db4(request):
    titulo = 'Dasboard 4'
    return render(request,'app_site/dashboard4.html', {'titulo': titulo})

def faq(request):
    titulo = 'Faq'
    return render(request,'app_site/faq.html', {'titulo': titulo})

def about(request):
    titulo = 'Sobre o Projeto'
    return render(request,'app_site/sobre.html', {'titulo': titulo})



# Create your views here.
