from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^(?P<idusuario>[-\w ]+)/(?P<nome>\w+)/$', views.login, name="Login"),
    url(r'^Finalizar/', views.finalizar, name="Finalizar"),
    url(r'^Limpar/', views.limpar, name="Limpar"),
    url(r'^Carrinho/', views.carrinho, name="Carrinho"),
]