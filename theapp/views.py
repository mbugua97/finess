from django.shortcuts import render,redirect
from . frm import FUser

def pageone(request):
    forms=FUser()
    context={'form':forms}
    return render(request,"theapp/firstpage.html",context)

def login(request):
    
    return render(request,'theapp/login.html')
    
def newuser(request):
    return render(request,'theapp/newuser.html')
