from models import *


def adicionaCarrinho(idusuario, nome):
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
