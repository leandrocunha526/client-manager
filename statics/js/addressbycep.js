$(document).ready(function() {
    $('#id_postal_code').keyup(function() {
        var postalCode = $(this).val().replace('-', ''); // Remove hyphens
        if (postalCode.length === 8) {
            $.getJSON('https://viacep.com.br/ws/' + postalCode + '/json/', function(data) {
                if (!("erro" in data)) {
                    $('.street_address').val(data.logradouro);
                    $('.district').val(data.bairro);
                    $('.city').val(data.localidade);
                    $('.state').val(data.uf);
                }
            });
        }
    });
});
