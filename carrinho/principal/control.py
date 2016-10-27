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

def adicionaProduto(idusuario, id_produto, nome, valor):
    try:
        produto=Carrinho.objects.get(idusuario= idusuario, produtos__produto__nome=nome)
    except:
        produto=Produto(nome=nome, categoria="teste", marca="teste2", preco=valor)
        Carrinho.objects(idusuario=idusuario).update(push__produtos=produto)
        print 'aaa\n'
    return produto
