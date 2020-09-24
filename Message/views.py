from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login, logout, get_user
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime

from Model.models import *

# Create your views here.

@login_required(login_url='Login')
def message(request, id):
    recepteur = Author.objects.get(id=id)
    username_recepteur = recepteur.user.username
    user_connecte = Author.objects.get(user=request.user)
    z = get_user(request).get_username()
    sms_send = Message.objects.filter(author_sms_username=user_connecte.user.username, recepteur_sms_username=recepteur.user.username)
    sms_recu = Message.objects.filter(recepteur_sms_username=user_connecte.user.username, author_sms_username=recepteur.user.username)
    a = datetime.datetime.now()
    form = MessageForm(request.POST or None, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            image_sms = form.cleaned_data['image_sms']
            contenu_sms = form.cleaned_data['contenu_sms']
            date_sms = form.cleaned_data['date_sms']
            author_sms_username = z
            recepteur_sms_username = form.cleaned_data['recepteur_sms_username']
            form.save()
            return redirect('sms', id)
    return render(request, 'Message/sms.html', locals())

@login_required(login_url='Login')
def statut(request):
    a = datetime.datetime.now()
    z = get_user(request).get_username()
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    statut = Statut.objects.filter(date_statut__gt=yesterday)
    user_connecte = Author.objects.get(user=request.user)
    statuts = Statut.objects.all()
    auteur = Author.objects.all()

    form = StatutForm(request.POST or None, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            date_statut = form.cleaned_data['date_statut']
            image_statut = form.cleaned_data['image_statut']
            contenu_statut = form.cleaned_data['contenu_statut']
            author_statut_username = form.cleaned_data['author_statut_username']
            form.save()
            return redirect("statut")
    return render(request, 'Message/statut.html', locals())


def Bot(request):
    return render(request, "Model/bot.html", locals())