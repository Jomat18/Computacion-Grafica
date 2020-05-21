$(document).ready(function() {

    $('form').on('submit', function(event) {
        event.preventDefault();
        var propiedad = document.getElementById("file").files[0];
        
        var nombre_imagen = propiedad.name;
        var extension_image = nombre_imagen.split('.').pop().toLowerCase();
        if(jQuery.inArray(extension_image, ['gif', 'png', 'jpg', 'jpeg']) == -1)
        {
            alert("No es un archivo de imagen");
        }
        var image_size = propiedad.size;
        if(image_size > 2000000) {
            alert("La imagen es muy grande");
        }
        else {
            var form_data = new FormData();
            form_data.append("file", propiedad);

            $.ajax({
                data : form_data,
                type : 'POST', 
                url: '/calcular',
                contentType: false,
                cache: false,
                processData: false,
                beforeSend: function(){
                    $('#cargando').html("<label style='color: green;'>Cargando imagen...</label>");
                }
            })
            .done(function(data) {
                if(data.error) {
                    console.log("Error");
                }
                else {
                    $("#imagen").prop("src", '/static/images/' + data.name);
                    $('#cargando').html(data);
                }
            });
        }
    });     
});