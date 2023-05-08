// Acessando o elemento HTML do campo de entrada pelo ID
let input = document.getElementById("inputFolderName");

// Adicionando um evento de escuta para verificar a entrada do usuário
input.addEventListener("input", function(event) {
  let valor = input.value;
  let letras = /^[a-zA-Z0-9_]+$/;
  if (!letras.test(valor)) {
    input.classList.add("is-invalid"); // Adicionando a classe "is-invalid" para aplicar estilo CSS
  } else {
    input.classList.remove("is-invalid"); // Removendo a classe "is-invalid" caso o valor seja válido
  }
});

