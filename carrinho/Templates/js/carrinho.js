function acertaTamanho() {
  if (window.innerWidth > 960) {
    document.getElementById("divBackground").style.height = ((440 + 180*numProdutos) + "px");
    document.getElementById("divCarrinho").style.height = ((400 + 180*numProdutos) + "px");
    document.getElementById("corpo").style.height = ((470 + 180*numProdutos) + "px");
  }
  else {
    document.getElementById("divBackground").style.height = ((500 + 250*numProdutos) + "px");
    document.getElementById("divCarrinho").style.height = ((460 + 250*numProdutos) + "px");
    document.getElementById("corpo").style.height = ((530 + 250*numProdutos) + "px");
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
