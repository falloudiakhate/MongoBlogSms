from django.shortcuts import render, redirect, reverse
from .forms import *
from django.contrib.auth.forms import UserCreationForm

from .forms import UserForm, LoginForm
from .models import *

from django.contrib.auth import authenticate, login, logout

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.decorators import login_required

import datetime

# Create your views here.

def Registration(request):
    
        if request.method == "POST":
    
            userform = UserForm(request.POST, request.FILES)
            authorform = AuthorForm(request.POST, request.FILES)

            # if form.is_valid():
            if userform.is_valid() and authorform.is_valid():

                    user = userform.save()
                    author = authorform.save(commit=False)
                    author.user = user
                    author.save()
                    
                    return redirect("Login")
                
            userform = UserForm()
            authorform = AuthorForm()
            return render(request, "Model/registration.html", locals())

        
        userform = UserForm()
        authorform = AuthorForm()
        return render(request, "Model/registration.html", locals())
    

       
def Login(request):

        if request.method == "POST":
    
            form = LoginForm(request.POST)

            if form.is_valid():

                  username = form.cleaned_data.get("username")
                  password = form.cleaned_data.get("password")

                  user = authenticate(username = username, password = password)

                  if user:

                        login(request, user)
                        return redirect("UserProfil")

                  else:

                        form = LoginForm()
                        return render(request, "Model/login.html", locals())

        form = LoginForm()
        return render(request, "Model/login.html", locals())
         
        
                
    
def Logout(request):
    
      logout(request)
      return redirect(reverse('HomePage'))


def SetPassword(request):
        
    if request.method=='POST':
            
        form=PasswordForm(request.POST)
        
        if form.is_valid():
                
            password=form.cleaned_data['password']
            email=form.cleaned_data['email']
            user=User.objects.get(email=email)
            user.set_password(password) 
            user.save()
                
            return redirect('Login')  
    
        form = LoginForm()
        return render(request, "Model/password.html", locals())

    form = LoginForm()
    return render(request, "Model/password.html", locals())

@login_required(login_url='Login')
def UserProfil(request):
    
    my_post = Post.objects.filter(author=request.user.author)
    
    friend = Author.objects.exclude(user=request.user)
    con_user=Author.objects.get(user=request.user)
    a = datetime.datetime.now()
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    notification = Message.objects.filter(recepteur_sms_username=con_user.user.username, date_sms__gt=yesterday)
    send = Message.objects.filter(author_sms_username=con_user.user.username)
    a = b = 0
    for i in send:
        a += 1
    receive = Message.objects.filter(recepteur_sms_username=con_user.user.username)
    for j in receive:
        b += 1
    
    page = request.GET.get('page', 1)

    paginator = Paginator(friend, 5)
    try:
            friend = paginator.page(page)
    except PageNotAnInteger:
            friend = paginator.page(1)
    except EmptyPage:
            friend = paginator.page(paginator.num_pages)
    
    return render(request, "Model/userprofile.html", locals())




    
    
def UpdateProfile(request):
        
        
        up_auth = Author.objects.get(user=request.user)
    

    
        if request.method == "POST":
    
            userform = UserForm(request.POST, request.FILES,  instance=request.user)
            authorform = AuthorForm(request.POST, request.FILES, instance=up_auth)

            # if form.is_valid():
            if userform.is_valid() and authorform.is_valid():

                    user = userform.save()
                    author = authorform.save(commit=False)
                    author.user = user
                    author.save()
                    
                    # return redirect("UserProfil")
                
            userform = UserForm(instance=request.user)
            authorform = AuthorForm(instance=up_auth)
            context = {'auteur' : userform}
            return render(request, "Model/userprofile.html",context, locals())

        
        userform = UserForm(instance=request.user)
        authorform = AuthorForm(instance=up_auth)
        return render(request, "Model/userprofile.html", locals())


def MoreDetails(request, id):
        more = Author.objects.get(id=id)
        return render(request, "Model/moredetails.html", locals())
    
def Blog(request):
    return render(request, "Model/blog.html", locals())