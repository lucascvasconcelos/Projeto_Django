from django.conf.urls import url
from forum import views
from forum import models


urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^post/(?P<pk>\d+)/$', views.ver_post, name = 'ver_post'),
    url(r'^novo_post/$', views.editar_post, name='novo_post'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.editar_post, name = 'editar_post'),
    url(r'^comentario/$', views.comentar, name = 'comentario')
]   
