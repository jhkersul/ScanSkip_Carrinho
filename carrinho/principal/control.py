from models import *
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR + '/carrinho/produtos/')
from produtos.models import Produto

def verificaUsuario(request):
    try:
        logado = request.session['logado']
    except KeyError:
        request.session['logado'] = False
        logado = False
    return logado


def pegaCarrinho(idusuario, nome):
    if nome == None:
        carrinho = Carrinho.objects.get(idusuario=idusuario)
    else:
        try:
            carrinho = Carrinho.objects.get(idusuario=idusuario, nome=nome)
        except:
            carrinho = Carrinho(idusuario=idusuario, nome=nome)
            carrinho.save()
    return carrinho

def limpaCarrinho(carrinho):
    carrinho.produtos.delete()  # Verificar isso (Garantir que remove todos os produtos, deixando a lista vazia)
    carrinho.save()
    return carrinho

def pegaTotal(carrinho):
    total = 0
    for produto in carrinho.produtos:
        total += float(produto.preco.replace(',', '.'))
    total = 'R$ ' + ('%.2f' % (float(total))).replace('.', ',')
    return total

def pegaTotalFloat(carrinho):
    total = 0
    for produto in carrinho.produtos:
        total += float(produto.preco.replace(',', '.'))
    return total


def deletaCarrinho(carrinho):
    carrinho.delete()


def adicionaProduto(idusuario, idProduto, nome, marca, categoria, preco, imagem):
    try:
        produto = Carrinho.objects.get(idusuario=idusuario, produtos__produto__idProduto=idProduto)
    except:
        produto = Produto(idProduto=idProduto, nome=nome, categoria=categoria, marca=marca, preco=preco, imagem=imagem, quantidade=1)
        Carrinho.objects(idusuario=idusuario).update(add_to_set__produtos=produto)
    return produto


def removeProduto(idusuario, idProduto):
    Carrinho.objects(idusuario=idusuario).update_one(pull__produtos__idProduto=idProduto)


def pegaAltura(carrinho):
    altura = 240
    for produto in carrinho.produtos:
        altura += 180
    altura = max(altura, 420)
    return altura
