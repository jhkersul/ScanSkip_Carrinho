from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^id=(?P<idProduto>[-\w ]+)/', views.produto, name="Produto"),
    url(r'^TesteProduto/', views.testeProduto, name="TesteProduto"),
]
