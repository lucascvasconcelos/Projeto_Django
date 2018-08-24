# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now

from django.http import HttpResponse
from forum import models
from forum import forms
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
# Create your views here.



def index(request):
    return render(
        request,
        'index.html',
        {'posts': models.Post.objects.all(),
        'titulo': u'Forum bugado'}
        )

def ver_post(request, pk):
    post = get_object_or_404(models.Post, pk = pk)
    return render(
        request,
        'ver_post.html',
        {'post': post, 'titulo': post.titulo}
        )


@login_required
def editar_post(request, pk):
    if pk:
        post = get_object_or_404(models.Post, pk = pk)
        if post.usuario != request.user:
            raise PermissionDenied
    else:
        post = None

 
    
    if request.method == 'POST':
        dados = request.post
    else:
        dados = None

    form = forms.PostForm(dados, instance = post, initial={"usuario": request.user.id})
    form.fields['usuario'].queryset = User.objects.filter(id = request.user.id)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'form.html',{'form': form})

def comentar(request, pk = None):
    if request.method == 'POST':
        dados = request.post
    else:
        dados = None

    coment = get_object_or_404(models.Post, pk = pk)