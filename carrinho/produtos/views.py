from django.shortcuts import render
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR + '/carrinho/utils/')
from utils.network import Network
from django.http import JsonResponse


def produto(request, idProduto):
    urlProduto = 'http://127.0.0.1:8000/produtos/TesteProduto' #'http://143.107.102.49:3000/produto/' + idProduto
    network = Network()
    response = network.request(urlProduto, 'GET')
    nome = response['nome']
    marca = response['marca']
    preco = response['valor']
    preco = ('%.2f' % (float(preco)/100)).replace('.', ',')
    categoria = response['categoria']
    imagem = response['imagem']
    return render(request, 'produto-escaneado-confirmacao.html', {'idProduto': idProduto, 'nome': nome, 'marca': marca, 'preco': preco, 'categoria': categoria, 'imagem': imagem})


def testeProduto(request):
    dicionario = {'idProduto': '12', 'nome': 'Agua Desidratada', 'valor': '1499', 'marca': 'Cristal', 'categoria': 'Consumo', 'imagem': 'http://charges.uol.com.br/upload/bobagens/aguad.jpg'}
    return JsonResponse(dicionario)
