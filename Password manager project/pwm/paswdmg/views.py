from django.shortcuts import render,HttpResponse
from paswdmg.models import Login,DataBasePass
# Create your views here.

def index(req):
    return render(req,'home.html')

def login(req):
    if req.method == "POST":
        email = req.POST.get('email')
        password = req.POST.get('password')
        login = Login(email=email,password=password)
        login.save()
    return render(req,'index.html')

def logout(req):
    return HttpResponse('Logout')

def database(req):
    if req.method == "POST":
        emailtosave = req.POST.get('emailtosave')
        passwordtosave = req.POST.get('passwordtosave')
        website = req.POST.get('website')
        name = req.POST.get('name')
        dbsave = DataBasePass(emailtosave=emailtosave,website=website,passwordtosave=passwordtosave,name=name)
        dbsave.save()
        return render(req,'database.html')

    return render(req,'database.html')

def returnin(req):
    return render(req,'return.html')


