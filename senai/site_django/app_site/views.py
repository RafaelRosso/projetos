from django.shortcuts import render


def index(request):
    return render(request,'app_site/index.html')

def db1(request):
    return render(request,'app_site/dashboard1.html')

def db2(request):
    return render(request,'app_site/dashboard2.html')

def db3(request):
    return render(request,'app_site/dashboard3.html')

def db4(request):
    return render(request,'app_site/dashboard4.html')

def faq(request):
    return render(request,'app_site/faq.html')

def about(request):
    return render(request,'app_site/sobre.html')



# Create your views here.
