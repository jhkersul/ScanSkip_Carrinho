from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from control import *
from django.core.serializers import *
from rest_framework.views import APIView
from django.http import JsonResponse
from mongoengine.django.sessions import MongoSession
import urllib
import sys
import os
import json
from utils.network import Network
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR + '/carrinho/utils/')

siteFila = 'https://webteste-d2bec.firebaseapp.com/tempodeespera.html?preferencial='
sitePrincipal = 'https://scan-skip-teste.herokuapp.com/'


def login(request, idusuario, nome):
    carrinho = pegaCarrinho(idusuario, nome)
    request.session['logado'] = True
    request.session['nome'] = nome
    request.session['idusuario'] = idusuario
    numProdutos = len(carrinho.produtos)
    return HttpResponseRedirect(sitePrincipal + 'perfil')


def logout(request):
    logado = verificaUsuario(request)
    if logado:
        del request.session['logado']
        del request.session['nome']
        del request.session['idusuario']
        MongoSession.objects.get(session_key=request.session.session_key).delete()
    return HttpResponseRedirect(sitePrincipal + 'logout')


def finalizar(request):
    logado = verificaUsuario(request)
    if logado:
        carrinho = pegaCarrinho(request.session['idusuario'], request.session['nome'])
        atualizaQuantidades(carrinho, request)
        total = pegaTotal(carrinho)
        totalFloat = float(total.replace('R$ ', '').replace(',', '.'))
        return render(request, 'seletor-forma-de-pagamento.html', {'total': total, 'totalFloat': totalFloat})
    else:
        return redirect(sitePrincipal + 'login')


def fila(request):
    logado = verificaUsuario(request)
    if logado:
        carrinho = pegaCarrinho(request.session['idusuario'], request.session['nome'])
        atualizaQuantidades(carrinho, request)
        urlFila = siteFila + "0?myVar=" + request.session['idusuario']
        return HttpResponseRedirect(urlFila)
    else:
        return redirect(sitePrincipal + 'login')

def filaPref(request):
    logado = verificaUsuario(request)
    if logado:
        carrinho = pegaCarrinho(request.session['idusuario'], request.session['nome'])
        atualizaQuantidades(carrinho, request)
        urlFila = siteFila + "1?myVar=" + request.session['idusuario']
        return HttpResponseRedirect(urlFila)
    else:
        return redirect(sitePrincipal + 'login')


def limpar(request):
    logado = verificaUsuario(request)
    if logado:
        carrinho = pegaCarrinho(request.session['idusuario'], request.session['nome'])
        carrinho = limpaCarrinho(carrinho)
        numProdutos = len(carrinho.produtos)
        response = render(request, 'carrinho.html', {'carrinho': carrinho, 'numProdutos': numProdutos})
        cookies = json.dumps({})
        cookieString = urllib.quote(cookies)
        response.set_cookie('produtos', cookieString)
        return response
    else:
        return redirect(sitePrincipal + 'login')


def carrinho(request):
    logado = verificaUsuario(request)
    if logado:
        carrinho = pegaCarrinho(request.session['idusuario'], request.session['nome'])
        numProdutos = len(carrinho.produtos)
        atualizaQuantidades(carrinho, request)
        return render(request, 'carrinho.html', {'carrinho': carrinho, 'numProdutos': numProdutos})
    else:
        return redirect(sitePrincipal + 'login')


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
        carrinho = pegaCarrinho(request.session['idusuario'], request.session['nome'])
        atualizaQuantidades(carrinho, request)
        if 'botaoAdicionar' in request.POST:
            idProduto = request.POST.get('idProduto')
            nome = request.POST.get('nome')
            marca = request.POST.get('marca')
            categoria = request.POST.get('categoria')
            preco = request.POST.get('preco')
            imagem = request.POST.get('imagem')
            quantidade = request.POST.get('quantidade')
            produto = adicionaProduto(request.session['idusuario'], idProduto, nome, marca, categoria,  preco, imagem, quantidade)
        carrinho = pegaCarrinho(request.session['idusuario'], request.session['nome'])
        numProdutos = len(carrinho.produtos)
        return render(request, 'carrinho.html', {'carrinho': carrinho, 'numProdutos': numProdutos})
    else:
        return redirect(sitePrincipal + 'login')


def remove(request):
    logado = verificaUsuario(request)
    if logado:
        carrinho = pegaCarrinho(request.session['idusuario'], request.session['nome'])
        atualizaQuantidades(carrinho, request)
        idProduto = request.POST.get('idProduto')
        removeProduto(request.session['idusuario'], idProduto)
        cookies = getCookies(request)
        cookies.pop(idProduto, None)
        cookies = json.dumps(cookies)
        cookieString = urllib.quote(cookies)
        carrinho = pegaCarrinho(request.session['idusuario'], request.session['nome'])
        numProdutos = len(carrinho.produtos)
        response = render(request, 'carrinho.html', {'carrinho': carrinho, 'numProdutos': numProdutos})
        response.set_cookie('produtos', cookieString)
        return response
    else:
        return redirect(sitePrincipal + 'login')


def produtos(request, idusuario):
    carrinho = pegaCarrinho(idusuario, None)
    listaJson = []
    for produto in carrinho.produtos:
        listaJson.append({'idProduto' : produto.idProduto,'nome' : produto.nome,'categoria' : produto.categoria,'marca' : produto.marca,'preco' : produto.preco,'imagem' : produto.imagem,'quantidade' : produto.quantidade})
	return JsonResponse(listaJson, safe=False)

def mapa(request):
    idProduto = request.GET.get("idProduto", None)
    markedSectors = []

    if idProduto is not None:
        urlSetoresProduto = 'https://scan-skip-plu-teste.herokuapp.com/setoresProduto/' + idProduto
        network = Network()
        response = network.request(urlSetoresProduto, 'GET')
        if response != -1:
            for setor in response :
                markedSectors.append(setor['idSetor'])


    return render(request, 'mapa.html', {'markedSectors' : markedSectors, 'sectorsRange': range(1, 53)})
