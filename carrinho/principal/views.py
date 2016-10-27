from django.shortcuts import render
from django.http import HttpResponseRedirect
from control import *
from django.core.serializers import *
from rest_framework.views import APIView
from django.http import JsonResponse
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR + '/carrinho/utils/')
from utils.network import Network


def login(request, idusuario, nome):
    carrinho = adicionaCarrinho(idusuario, nome)
    request.session['logado'] = True
    request.session['nome'] = nome
    request.session['idusuario'] = idusuario
    request.session['urlToda'] = 'https://webteste-d2bec.firebaseapp.com/tempodeespera.html?myVar='+idusuario
    return render(request, 'carrinho.html', {'carrinho': carrinho})


# def finalizar(request):
#     urlFila = 'http://www.google.com.br/'
#     params = {'idusuario': request.session['idusuario'], 'preferencial': False}
#     network = Network()
#     resposta = network.request(urlFila, 'POST', params)
#     urlFila = 'http://www.google.com.br/' + request.session['idusuario']
#     return HttpResponseRedirect(urlFila)


def limpar(request):
    carrinho = adicionaCarrinho(request.session['idusuario'], request.session['nome'])
    carrinho = limpaCarrinho(carrinho)
    return render(request, 'carrinho.html', {'carrinho': carrinho})


def carrinho(request):
    carrinho = adicionaCarrinho(request.session['idusuario'], request.session['nome'])
    return render(request, 'carrinho.html', {'carrinho': carrinho})


def total(request, idusuario):
    carrinho = adicionaCarrinho(idusuario, None)
    total = pegaTotal(carrinho)
    dicionario = {'idusuario': idusuario, 'total': total}
    return JsonResponse(dicionario)


def fim(request, idusuario):
    carrinho = adicionaCarrinho(idusuario, None)
    deletaCarrinho(carrinho)
    dicionario = {'idusuario': idusuario, 'fim': True}
    return JsonResponse(dicionario)
