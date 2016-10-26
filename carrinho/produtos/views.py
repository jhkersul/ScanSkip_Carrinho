from django.shortcuts import render

# Create your views here.
def produto(request, id_produto):
    request.session['id_produto'] = id_produto
    return render(request, 'produto-escaneado-confirmacao.html')

