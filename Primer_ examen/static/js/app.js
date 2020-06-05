$(document).ready(function() {

    $('#valor_1').hide();
    $('#valor_2').hide();
    $('#valor_r').hide();
    $('#out').hide();

    $("#operador").on('change',  function (event) {

        if (this.value=="raizC") {
            $("#label_1").text("C");
            $("#label_r").text("R");
            $('#valor_1').show();
            $('#out').show();
            $('#valor_r').show();

            $('#valor_2').hide();
            $("#label_2").text("");
        
        }
        else if(this.value=="exponencial") {
            $("#label_1").text("C");
            $('#valor_1').show();
            $('#out').hide();
            $('#valor_r').hide();
            $("#label_r").hide();
            $("#label_2").text("B");
            $('#valor_2').show();
        }
        else if(this.value=="logaritmo") {
            $("#label_1").text("C");
            $("#label_r").text("");
            $('#valor_1').show();
            $('#out').hide();
            $('#valor_r').hide();

            $('#valor_2').hide();
            $("#label_2").text("");
        
        }
        else if(this.value=="equalizacion") {
            $('#valor_1').hide();
            $('#valor_2').hide();
            $('#valor_r').hide();
            $('#out').hide();
            $("#label_1").text("");
            $("#label_2").text("");
            $("#label_r").text("");
        }
        else if(this.value=="contrast") {
            $("#label_1").text("%");
            $("#label_r").text("");
            $('#valor_1').show();
            $('#out').hide();
            $('#valor_r').hide();

            $('#valor_2').hide();
            $("#label_2").text("");
        }
        else if(this.value=="thresholding") {
            $("#label_1").text("min");
            $("#label_2").text("max");
            $('#valor_1').show();
            $('#valor_2').show();
            $('#out').hide();
            $('#valor_r').hide();
            $("#label_r").text("");
        } 
        
        else { // adicion o division
            $('#valor_1').hide();
            $('#valor_2').hide();
            $('#valor_r').hide();
            $('#out').hide();
            $("#label_1").text("");
            $("#label_2").text("");
            $("#label_r").text("");
        }
       
    });

    $("#file").on('change', function (event){

        $("#cuadro").removeClass("temp");

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
                processData: false
            })
            .done(function(data) {
                if(data.error) {
                    console.log("Error");
                }
                else {
                    $("#imagen").prop("src", '/static/images/' + data.name);
                }
            });
        }        
    });

    $('form').on('submit', function(event) {
        event.preventDefault();     
        $.ajax({ 
            url: '/calcular',
            data: { valor_1: $('#valor_1').val(),
                    valor_2: $('#valor_2').val(),
                    valor_r: $('#valor_r').val(),
                    operador: $('#operador').val()
                },
            type: 'POST'
        }).done(function(data) {
            var source = '/static/images/' +data.name,
            timestamp = (new Date()).getTime(),
            newUrl = source + '?_=' + timestamp;
            document.getElementById("imagen").src = newUrl;
            
        }).fail(function() {
            console.log('Failed');
        });        
    });     

});