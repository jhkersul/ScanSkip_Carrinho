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

  $('#myModal').on('shown.bs.modal', function () {
    $('#myInput').focus()
  })

  $(function() {
    var options = {
      byRow: true,
      property: 'height',
      target: null,
      remove: false
    }
    $('.modal-child').matchHeight(options);
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

// Pega os produtos do PLU
function getProducts(idSetor) {
  // Setando HTMLs iniciais para começarmos a dar loading nos produtos
  $('#products-container').html("");
  $('#myModalLabel').html("Setor " + idSetor);

  // Mostrando loading
  showLoading();

  // Carregando produtos
  $.getJSON( "https://scan-skip-plu-teste.herokuapp.com/produtosSetor/" + idSetor, function( data ) {
    // Se tivermos resultados, data vai ser diferente de -1
    if (data != -1) {
      var productsRendered = [];

      for (index in data) {
        // Renderizando o template com o Mustache
        Mustache.tags = ['[[', ']]'];
        var template = $('#template').html();
        Mustache.parse(template);
        var price = (data[index]['valor']/100).toFixed(2);
        var product = {
          name: data[index]['nome'],
          brand: data[index]['marca'],
          price: price,
          category: data[index]['categoria'],
          image: data[index]['imagem'],
        }
        var rendered = Mustache.render(template, product);
        productsRendered.push(rendered);
      }

      // Colocando todos os produtos renderizados dentro de 'products-container'
      $('#products-container').html(productsRendered);
    } else {
      // Caso nenhum produto seja encontrado, é gerado um aviso para o usuário
      $('#products-container').html("Nenhum produto encontrado neste setor.");
    }

    // Escondendo o loading
    hideLoading();
  });

}

function toDataUrl(src, callback, outputFormat) {
  var img = new Image();
  img.crossOrigin = 'Anonymous';
  img.onload = function() {
    var canvas = document.createElement('CANVAS');
    var ctx = canvas.getContext('2d');
    var dataURL;
    canvas.height = this.height;
    canvas.width = this.width;
    ctx.drawImage(this, 0, 0);
    dataURL = canvas.toDataURL(outputFormat);
    callback(dataURL);
  };
  img.src = src;
  if (img.complete || img.complete === undefined) {
    img.src = "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///ywAAAAAAQABAAACAUwAOw==";
    img.src = src;
  }
}

function showLoading() {
    $("#loading").show();
}

function hideLoading() {
    $("#loading").hide();
}
