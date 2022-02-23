from django.shortcuts import render, redirect
from .models import Names
from .forms import SignUpForm, Userauth
from django.contrib.auth import login as loginauth, logout as logoutsite,authenticate
from rest_framework.generics import GenericAPIView
from rest_framework import generics

from .models import Images
from .api import Imagess


# Create your views here.
def BaseSite(request):
    data = Names.objects.all()
    return render(request, 'FilesHtml/base.html',{"data":data})


def NamesByid(request,Id_name):
    data = Names.objects.get(id=Id_name)
    return render(request, 'FilesHtml/nameByid.html',{"data":data})

def Azkar(request):
    return render(request, 'FilesHtml/Azkar.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            loginauth(request, user)
            return redirect('http://127.0.0.1:7000/')
    else:
        form = SignUpForm()
    return render(request, 'FilesHtml/signup.html', {'form': form})




def loginbase(request):
    form = Userauth
    if (request.method == 'GET'):
        return render(request, 'FilesHtml/login.html', {'form': form})

    else:
       user = authenticate(username=request.POST['username'],password=request.POST['password'])
       print(user)
       if (user):
           loginauth(request,user)
           return redirect('/')

    return render(request, 'FilesHtml/login.html')



def logOut(request):
    logoutsite(request)

    # return render(request,'demo/login.html')
    return redirect('login')



class image(generics.ListCreateAPIView):
    queryset = Images.objects.all()
    serializer_class = Imagess