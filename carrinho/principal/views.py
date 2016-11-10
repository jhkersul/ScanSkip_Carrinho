from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from control import *
from django.core.serializers import *
from rest_framework.views import APIView
from django.http import JsonResponse
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR + '/carrinho/utils/')

siteFila = 'https://webteste-d2bec.firebaseapp.com/tempodeespera.html?myVar='
siteLogin = 'http://143.107.102.52:8000/cadastro/login'


def login(request, idusuario, nome):
    carrinho = pegaCarrinho(idusuario, nome)
    request.session['logado'] = True
    request.session['nome'] = nome
    request.session['idusuario'] = idusuario
    numProdutos = len(carrinho.produtos)
    return render(request, 'carrinho.html', {'carrinho': carrinho, 'numProdutos': numProdutos})


def finalizar(request):
    urlFila = siteFila + request.session['idusuario']
    return HttpResponseRedirect(urlFila)


def limpar(request):
    logado = verificaUsuario(request)
    if logado:
        carrinho = pegaCarrinho(request.session['idusuario'], request.session['nome'])
        carrinho = limpaCarrinho(carrinho)
        numProdutos = len(carrinho.produtos)
        return render(request, 'carrinho.html', {'carrinho': carrinho, 'numProdutos': numProdutos})
    else:
        return redirect(siteLogin)


def carrinho(request):
    logado = verificaUsuario(request)
    if logado:
        carrinho = pegaCarrinho(request.session['idusuario'], request.session['nome'])
        total = pegaTotal(carrinho)
        totalFloat = pegaTotalFloat(carrinho)
        altura1 = pegaAltura(carrinho)
        numProdutos = len(carrinho.produtos)
        return render(request, 'carrinho.html', {'carrinho': carrinho, 'total': total, 'totalFloat': totalFloat, 'numProdutos': numProdutos, 'altura1': altura1, 'altura2': altura1+30})
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
<<<<<<< HEAD
        total = pegaTotal(carrinho)
        altura1 = pegaAltura(carrinho)
        totalFloat = pegaTotalFloat(carrinho)
        return render(request, 'carrinho.html', {'carrinho': carrinho, 'totalFloat': totalFloat, 'total': total, 'altura1': altura1, 'altura2': altura1+30})
=======
        numProdutos = len(carrinho.produtos)
        return render(request, 'carrinho.html', {'carrinho': carrinho, 'numProdutos': numProdutos})
>>>>>>> f0738d6b15db2f58d3170c875804ccfeca01bb41
    else:
        return redirect(siteLogin)


def remove(request):
    logado = verificaUsuario(request)
    if logado:
        idProduto = request.POST.get('idProduto')
        removeProduto(request.session['idusuario'], idProduto)
        carrinho = pegaCarrinho(request.session['idusuario'], request.session['nome'])
        numProdutos = len(carrinho.produtos)
        return render(request, 'carrinho.html', {'carrinho': carrinho, 'numProdutos': numProdutos})
    else:
        return redirect(siteLogin)


def soma(request):  # Falta testar
    logado = verificaUsuario(request)
    if logado:
        idProduto = request.POST.get('idproduto')
        quantidade = somaProduto(request.session['idusuario'], idProduto)
        return HttpResponse(str(quantidade))
    else:
        return redirect(siteLogin)


def subtrai(request):   # Falta testar
    logado = verificaUsuario(request)
    if logado:
        idProduto = request.POST.get('idproduto')
        quantidade = subtraiProduto(request.session['idusuario'], idProduto)
        return HttpResponse(str(quantidade))
    else:
        return redirect(siteLogin)
