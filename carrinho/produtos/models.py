from django.db import models

from mongoengine import *

class Produto(EmbeddedDocument):
    nome = StringField(unique_with='marca', required=True)
    categoria = StringField(required=True)
    marca = StringField(required=True)
    preco = StringField(required=True)
