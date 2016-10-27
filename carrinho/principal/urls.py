from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^id=(?P<idusuario>[-\w ]+)/$', views.total, name="Total"),
    url(r'^id=(?P<idusuario>[-\w ]+)/nome=(?P<nome>\w+)/$', views.login, name="Login"),
    url(r'^Finalizar/', views.finalizar, name="Finalizar"),
    url(r'^Limpar/', views.limpar, name="Limpar"),
    url(r'^$', views.carrinho, name="Carrinho"),
    url(r'^nome=(?P<nome>\w+)/id_produto=(?P<id_produto>\w+)/valor=(?P<valor>\w+)/$', views.adiciona, name="Adicionar"),
]
