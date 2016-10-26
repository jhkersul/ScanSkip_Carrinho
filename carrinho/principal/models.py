from __future__ import unicode_literals

import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR + '/carrinho/produtos/')

from mongoengine import *
from produtos.models import Produto


class Carrinho(Document):
    idusuario = StringField(unique=True, required=True)
    nome = StringField(required=True)
    produtos = EmbeddedDocumentListField(Produto)
