from django.shortcuts import render ,redirect
from django.template import loader
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from .forms import login_forms,login_register
# Create your views here.def
def login_auth(request):
    if request.method=="POST":
      login_form =login_forms(request.POST)
      if login_form.is_valid():
        username =login_form.cleaned_data['username']
        pwd= login_form.cleaned_data['pwd']
        user=authenticate(username=username ,password=pwd)
        if user is not None:
          login(request ,user)
          return redirect('kevin')
        else :
          messages.error(request,'authentifications echouer')
          return render(request,'login.html',{'form':login_form})
      else:
        return render(request,'login.html',{'form':login_form})
     
    else :
     login_form =login_forms()
     return render(request,'login.html',{'form':login_form})
def register(request):
  if request.method =='POST':
    form =login_register(request.POST)
    if form.is_valid():
        username =form.cleaned_data['username']
        pwd =form.cleaned_data['pwd']
        #user =authenticate(username=username,password=pwd)
        if request:
          messages.error(request, 'erreur l\'utilisateur existe deja')
          form= login_register()
          return render(request,'register.html',{'form':form})
          pass
        else:
         user =User.objects.create_user(username=username,password=pwd)
        if user is not None:
          return redirect('login')

    username =form.cleaned_data['username']
    pwd =form.cleaned_data['pwd']
    user =authenticate(username=username,password=pwd)
    if user is not None:
      return redirect('login')

  else:
    form= login_register()
    return render(request,'register.html',{'form':form})
def logouts(request):
  logout(request)
  return redirect('login')