var deletaRow = (function (elemento) {
    elemento.preventDefault();
    alert('ola');
    $(elemento).closest('tr').remove();
});

function helow () {
    alert('ola');
}