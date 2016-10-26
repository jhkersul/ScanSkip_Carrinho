from .models import *
from rest_framework_mongoengine.serializers import DocumentSerializer

class CarrinhoSerializer(DocumentSerializer):
    class Meta:
        model = Carrinho