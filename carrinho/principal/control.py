from models import *


def adicionaCarrinho(idusuario, nome):
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
        total += float(produto.preco)
    return total

def deletaCarrinho(carrinho):
    carrinho.delete()