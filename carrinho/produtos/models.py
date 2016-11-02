from django.db import models

from mongoengine import *

class Produto(EmbeddedDocument):
    idProduto = StringField(unique=True, required=True)
    nome = StringField(required=True)
    categoria = StringField()
    marca = StringField(required=True)
    preco = StringField(required=True)
    imagem = StringField()

