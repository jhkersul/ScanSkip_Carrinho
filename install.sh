#!/bin/bash

## ESTE SCRIPT INSTALA AS BIBLIOTECAS NECESSÁRIAS PARA RODAR O PROJETO

echo "Installing Django..."
pip install Django
pip install djangorestframework
pip install django-filter

echo "Instalando requests..."
pip install requests

echo "Installing control..."
pip install control

echo "Installing markdown..."
pip install markdown

echo "Installing bliker..."
pip install blinker

echo "Installing mongo-engine"
pip install django-rest-framework-mongoengine
pip uninstall pymongo -y
pip install pymongo==2.8

echo "Installing whitenoise"
pip install whitenoise

echo "Installing mongoengine"
pip install mongoengine

echo "Installing corsheaders"
pip install django-cors-headers
