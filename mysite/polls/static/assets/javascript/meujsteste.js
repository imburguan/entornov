// Desenvolvimento Aberto
// Javascript teste

function meuMouseOver() {
    var div = document.getElementById('meulog');

    div.innerHTML = div.innerHTML + 'Você entrou no campo nome ';
}

function meuMouseOut() {
    var div = document.getElementById('meulog');

    div.innerHTML = div.innerHTML + 'Você saiu do campo nome ';
}
