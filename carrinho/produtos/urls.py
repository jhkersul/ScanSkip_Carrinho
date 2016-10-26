from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^(?P<id_produto>[-\w ]+)/', views.produto, name="Produto"),
]
