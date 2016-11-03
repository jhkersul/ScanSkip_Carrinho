from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^TesteProduto/', views.testeProduto, name="TesteProduto"),
    url(r'^(?P<idProduto>[-\w ]+)/', views.produto, name="Produto"),
]
