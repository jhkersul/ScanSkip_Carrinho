function acertaTamanho() {
  if (window.innerWidth > 960) {
    document.getElementById("divCarrinho").style.height = ((410 + 180*numProdutos) + "px");
    document.getElementById("corpo").style.height = ((480 + 180*numProdutos) + "px");
  }
  else {
    document.getElementById("divCarrinho").style.height = ((480 + 270*numProdutos) + "px");
    document.getElementById("corpo").style.height = ((550 + 270*numProdutos) + "px");
  }
}

function alteraQuantidade(op, idProduto) {
  if (op == "-" && produtos[idProduto]['quantidade'] > 1) {
    produtos[idProduto]['quantidade'] -= 1;
  }
  if (op == "+") {
    produtos[idProduto]['quantidade'] += 1;
  }

  setaQuantidade();
  setaValorTotal();
  salvaEstadoCarrinho();
}

function setaValorTotal() {
  const $valorTotal = $("#valortotal");

  var total = 0;
  for (var idProduto in produtos) {
    total += produtos[idProduto]['preco'] * produtos[idProduto]['quantidade'];
  }

  $valorTotal.html("R$ " + total.toFixed(2));
}

function salvaEstadoCarrinho() {
  // Limpando cookies
  Cookies.remove('produtos');

  Cookies.set('produtos', produtos);

  console.log(Cookies.get('produtos'));
}

function setaQuantidade() {
  for (let idProduto in produtos) {
    const $quantElement = $("#quantidade-" + idProduto);
    $quantElement.html(produtos[idProduto]['quantidade']);
  }
}
