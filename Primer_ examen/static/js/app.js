$(document).ready(function() {

    $("#file").on('change', function (event){
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
                url: '/mostrar',
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
                    $('#cargando').html("<label style='color: blue;'>Imagen Cargada!</label>");
                }
            });
        }        
    });

    $('form').on('submit', function(event) {
        event.preventDefault();  
        $.ajax({ 
            url: '/calcular',
            data: {

                    valor_t1: $('#t1').val(),
                    valor_t2: $('#t2').val(),
                    valor_minimo: $('#minimo').val(),
                    valor_maximo: $('#maximo').val(),
                    /*valor_a: $('#valor-a').val(),*/
                    valor_b: $('#valor-b').val(),
                    valor_c: $('#valor-c').val(),
                    valor_c_exp: $('#valor-c-exp').val(),
                    valor_c_rai: $('#valor-c-rai').val(),
                   // valor_d: $('#valor-d').val(),
                    valor_r: $('#valor-r').val(),
                    valor_intensidad: $('#intensidad').val(),
                    operador: $('#operador').val()
                },
            type: 'POST'
        })
        .done(function(data) {
        if(data.error) {
            console.log("Error");
        }
        else {
            $("#imagen").prop("src", '/static/output/' + data.name);
            $('#cargando').html("<label style='color: blue;'>Imagen procesada!</label>");
        }
    });
        
      /*  setTimeout(
              function() 
              {
                 $('#cargando').html("<label style='color: blue;'>Imagen cambio!</label>");

                 //$( "#imagen" ).removeData( "src" );
                 //$( "#imagen" ).data( "src", "/static/images/foto_junior.png" );
               // $("#imagen").prop("src", '/static/images/foto_junior.png');
               // $( "#imagen" ).remove();
                //$('.imagen').html('<img id="imagen" src="/static/output/resultado.png" />');
                $("#imagen").prop("src", '/static/output/resultado.png' );

              }, 3000);*/
       
       /*

        $.ajax({ 
            url: '/calcular',
            data: { valor_a: $('#valor-a').val(),
                    valor_b: $('#valor-b').val(),
                    valor_c: $('#valor-c').val(),
                    valor_d: $('#valor-d').val(),
                    valor_r: $('#valor-r').val(),
                    operador: $('#operador').val()
                },
            type: 'POST'
        }).done(function(data) {
            
            //$("#imagen").prop("src", '/static/images/' + data.name);
            $(".imagen").html("jejejej");
            $("#imagen").prop("src", '/static/images/molecula.jpeg');
        }).fail(function() {
            console.log('Failed');
        });      */  
    });     

});