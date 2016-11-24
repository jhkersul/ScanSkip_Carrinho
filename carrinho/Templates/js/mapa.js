$( document ).ready(function() {
  // Seleciona os setores já marcados inicialmente
  selectElement(markedSectors);

  // Clica em um setor no mapa
  $( ".element" ).click(function() {
    let idSetor = $(this).attr('id').replace("element-", "");
    selectElement([idSetor]);
    getProducts(idSetor);
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
      }
    }
  });

}
