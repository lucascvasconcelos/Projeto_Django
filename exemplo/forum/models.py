# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=1024, verbose_name=u'Título')
    conteudo = models.TextField(verbose_name=u'Conteúdo')
    usuario = models.ForeignKey(User, null = True, on_delete = models.SET_NULL, verbose_name=u'Usuário')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name=u'Data de criação')
   

    def __unicode__(self):
        return u'{} - {}'.format(self.titulo, self.data_criacao)



class Coments(models.Model):
    usuario = models.ForeignKey(User, verbose_name=u'Usuário')
    cometario = models.TextField(verbose_name = u'Comentário')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name=u'Data de criação')
    postId = models.ForeignKey(Post, null = False)
