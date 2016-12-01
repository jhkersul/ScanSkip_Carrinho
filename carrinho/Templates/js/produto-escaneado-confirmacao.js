$( document ).ready(function() {

});

var quantidade = 1;

function alteraQuantidade(op) {
  if (op == "-" && quantidade > 1) {
    quantidade -= 1;
  }
  if (op == "+") {
    quantidade += 1;
  }

  $("#qtdd").html(quantidade);
}
