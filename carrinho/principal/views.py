from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from control import *
from django.core.serializers import *
from rest_framework.views import APIView
from django.http import JsonResponse
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR + '/carrinho/utils/')

siteFila = 'https://webteste-d2bec.firebaseapp.com/tempodeespera.html?myVar='
siteLogin = 'http://www.google.com.br/'


def login(request, idusuario, nome):
    carrinho = pegaCarrinho(idusuario, nome)
    request.session['logado'] = True
    request.session['nome'] = nome
    request.session['idusuario'] = idusuario
    request.session['urlFila'] = siteFila+idusuario
    altura1 = pegaAltura(carrinho)
    return render(request, 'carrinho.html', {'carrinho': carrinho, 'total': 'R$ 0,00', 'altura1': altura1, 'altura2': altura1+30})


# def finalizar(request):
#     urlFila = 'http://www.google.com.br/'
#     params = {'idusuario': request.session['idusuario'], 'preferencial': False}
#     network = Network()
#     resposta = network.request(urlFila, 'POST', params)
#     urlFila = 'http://www.google.com.br/' + request.session['idusuario']
#     return HttpResponseRedirect(urlFila)


def limpar(request):
    logado = verificaUsuario(request)
    if logado:
        carrinho = pegaCarrinho(request.session['idusuario'], request.session['nome'])
        carrinho = limpaCarrinho(carrinho)
        total = pegaTotal(carrinho)
        altura1 = pegaAltura(carrinho)
        return render(request, 'carrinho.html', {'carrinho': carrinho, 'total': total, 'altura1': altura1, 'altura2': altura1+30})
    else:
        return redirect(siteLogin)


def carrinho(request):
    logado = verificaUsuario(request)
    if logado:
        carrinho = pegaCarrinho(request.session['idusuario'], request.session['nome'])
        total = pegaTotal(carrinho)
        totalFloat = pegaTotalFloat(carrinho)
        altura1 = pegaAltura(carrinho)
        return render(request, 'carrinho.html', {'carrinho': carrinho, 'total': total, 'totalFloat': totalFloat, 'altura1': altura1, 'altura2': altura1+30})
    else:
        return redirect(siteLogin)


def total(request, idusuario):
    carrinho = pegaCarrinho(idusuario, None)
    total = pegaTotal(carrinho)
    dicionario = {'idusuario': idusuario, 'total': total}
    return JsonResponse(dicionario)


def fim(request, idusuario):
    carrinho = pegaCarrinho(idusuario, None)
    deletaCarrinho(carrinho)
    dicionario = {'idusuario': idusuario, 'fim': True}
    return JsonResponse(dicionario)


def adiciona(request):
    logado = verificaUsuario(request)
    if logado:
        if 'botaoAdicionar' in request.POST:
            idProduto = request.POST.get('idProduto')
            nome = request.POST.get('nome')
            marca = request.POST.get('marca')
            categoria = request.POST.get('categoria')
            preco = request.POST.get('preco')
            imagem = request.POST.get('imagem')
            produto = adicionaProduto(request.session['idusuario'], idProduto, nome, marca, categoria,  preco, imagem)
        carrinho = pegaCarrinho(request.session['idusuario'], request.session['nome'])
        total = pegaTotal(carrinho)
        altura1 = pegaAltura(carrinho)
        return render(request, 'carrinho.html', {'carrinho': carrinho, 'total': total, 'altura1': altura1, 'altura2': altura1+30})
    else:
        return redirect(siteLogin)


def remove(request):
    logado = verificaUsuario(request)
    if logado:
        idProduto = request.POST.get('idProduto')
        removeProduto(request.session['idusuario'], idProduto)
        carrinho = pegaCarrinho(request.session['idusuario'], request.session['nome'])
        total = pegaTotal(carrinho)
        altura1 = pegaAltura(carrinho)
        return render(request, 'carrinho.html', {'carrinho': carrinho, 'total': total, 'altura1': altura1, 'altura2': altura1 + 30})
    else:
        return redirect(siteLogin)
