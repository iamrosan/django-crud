from django.shortcuts import render, redirect
from .models import Receipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request, 'vegetable/index.html')


@login_required(login_url='login')
def receipe(request):
    if request.method=='POST':
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe = Receipe(receipe_name=receipe_name, receipe_description=receipe_description, receipe_image=receipe_image)
        receipe.save()
        print(receipe_image)
        # print(data.receipe_name)
    return render(request,'vegetable/receipe.html')



@login_required(login_url='login')
def viewReceipe(request):
    receipes = Receipe.objects.all()
    if request.method=='POST':
        search_detail = request.POST['search_detail']
        print(search_detail)
        # query = 
        receipes = Receipe.objects.filter(receipe_name__icontains=search_detail)
    return render(request,'vegetable/receipeDetails.html',{'receipes':receipes})



@login_required(login_url='login')
def deleteReceipe(request, id):
   delete_query = Receipe.objects.get(id=id)
   delete_query.delete()
   return redirect('view-receipe')



@login_required(login_url='login')
def updateReceipe(request, id):
    update_query = Receipe.objects.get(id=id)
    context = {'receipe':update_query}
    if request.method == 'POST':
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        update_query.receipe_name=receipe_name
        update_query.receipe_description=receipe_description
        update_query.save()
        return redirect('view-receipe')
    return render(request,'vegetable/updateReceipe.html',context)


def login_user(request):
    if request.method == 'POST':
        data = request.POST
        username = data['username']
        password = data['password']

        # if User.objects.filter(username=username).exists():
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "INVALID USERNAME OR PASSWORD")
            return redirect('login')

        else:
            login(request, user)
            messages.info(request, "LOGIN SUCCESSFUL")
            return redirect('home')
            

    return render(request, 'vegetable/login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data['first_name']
        last_name = data['last_name']
        username= data['username']
        password = data['password']
        email = data['email']

        user_exist = User.objects.filter(username=username)

        if user_exist.exists():
            messages.info(request, "Username already Exits.")
            return redirect('signup')

        user = User(first_name=first_name, last_name=last_name, username=username)
        user.set_password(password)
        user.save()
        messages.info(request, "Your account is created.")
    return render(request, 'vegetable/register.html')