$( document ).ready(function() {
  // Seleciona os setores já marcados inicialmente
  selectElement(markedSectors);

  // Clica em um setor no mapa
  $( ".element" ).click(function() {
    let idSetor = $(this).attr('id').replace("element-", "");
    selectElement([idSetor]);
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
