$( document ).ready(function() {
  // Seleciona os setores já marcados inicialmente
  selectElement(markedSectors);

  // Clica em um setor no mapa
  $( ".element" ).click(function() {
    let idSetor = $(this).attr('id').replace("element-", "");
    selectElement([idSetor]);
    getProducts(idSetor);
    $("#myModal").modal();
  });
  //tentativa de apagar os produtos antigos pra quando clicar no outro setor o modal não manter tudo e ficar empilhando
  $("input#btClose").click(function(){
    var modalBody = document.getElementsByClassName("modal-body");
    $(".modal-body").val("");
  });

});


var currentSelected = [];
// Seleciona um elemento do mapa
function selectElement(indexes) {
  for (let i in currentSelected) {
    $("#element-" + currentSelected[i]).css("background-color", "rgba(113, 164, 225, 0.87)");
  }

  currentSelected = indexes;
  for (let j in indexes) {
    $("#element-" + indexes[j]).css("background-color", "rgba(204, 21, 0, 0.87)");
  }
}

function getProducts(idSetor) {
  $.getJSON( "https://scan-skip-plu-teste.herokuapp.com/produtosSetor/" + idSetor, function( data ) {
    if (data != -1) {
      for (index in data) {
        console.log("ID: " + data[index]['idProduto']);
        console.log("Nome: " + data[index]['nome']);
        console.log("Imagem: " + data[index]['imagem']);
        console.log("Marca: " + data[index]['marca']);
        console.log("Valor: " + data[index]['valor']);

        var nomeModal = document.getElementsByClassName('modal-title');
        nomeModal.innerHTML = data[index]['idProduto'];
        var divProduto = document.createElement('div');
        divProduto.id = index;
        divProduto.className = 'produtocarrinho';
        document.getElementsByClassName('modal-body')[0].appendChild(divProduto);

        var divInfo = document.createElement('div');
        divInfo.className = 'infocarrinho';
        divProduto.appendChild(divInfo);

        var infoNome = document.createElement('P');
        infoNome.className = 'nomeproduto';
        divInfo.appendChild(infoNome);
        infoNome.innerHTML = data[index]['nome'];
        
        var infoMarca = document.createElement('P');
        infoMarca.className = 'marcaproduto';
        divInfo.appendChild(infoMarca);
        infoMarca.innerHTML = data[index]['marca'];

        var infoPreco = document.createElement('P');
        infoPreco.className = 'precoproduto';
        divInfo.appendChild(infoPreco);
        infoPreco.innerHTML = data[index]['valor'];

        var produtoFoto = document.createElement('div');
        produtoFoto.className = 'fotoprodutocarrinho';
        divProduto.appendChild(produtoFoto);

        //tentativa de conversão do base64
        var base64imgC = data[index]['imagem'];
        console.log(base64imgC);

        var base64img = base64imgC.split(',')[1];
        console.log(base64img);

        var urls = window.atob(base64img);
        console.log(urls);

        produtoFoto.style.backgroundImage = base64imgC;


        //tentativa de mudar o titulo do modal pegando o nome da categoria que vem do PLU (mudado hoje)
        var modalTitle = document.getElementsById("myModalLabel");
        modalTitle.innerHTML = data[index]['categoria']

      }
    }
  }
  );

}
