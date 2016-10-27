from django.shortcuts import render
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR + '/carrinho/utils/')
from utils.network import Network
from django.http import HttpResponseRedirect

# Create your views here.
def produto(request, id_produto):
    urlProduto = 'http://143.107.102.49:3000/produto/' + id_produto
    network = Network()
    response = network.request(urlProduto, 'GET')
    nome = response['nome']
    preco = response['valor']
    preco = str(float(preco)/100).replace('.', ',')
    return render(request, 'produto-escaneado-confirmacao.html', {'nome': nome, 'preco': preco})

