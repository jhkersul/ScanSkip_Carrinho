from django.shortcuts import render
from control import *
from django.core.serializers import *
from rest_framework.views import APIView


def login(request, idusuario, nome):
    carrinho = adicionaCarrinho(idusuario, nome)
    request.session['logado'] = True
    request.session['nome'] = nome
    request.session['idusuario'] = idusuario



def finalizar(request):
    return carrinho(request)


def limpar(request):
    carrinho = adicionaCarrinho(request.session['idusuario'], request.session['nome'])
    carrinho = limpaCarrinho(carrinho)
    return render(request, 'carrinho.html', {'carrinho': carrinho})


def carrinho(request):
    carrinho = adicionaCarrinho(request.session['idusuario'], request.session['nome'])
    return render(request, 'carrinho.html', {'carrinho': carrinho})
