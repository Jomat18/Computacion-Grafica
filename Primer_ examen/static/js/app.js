var i = 1

$(document).on('click', '.remove-img', function () {
	$(this).parent().remove(); 
	i = i - 1

	if (i == 1) {
    	$("#cuadro").addClass("temp");
    }

    document.getElementById("file").value = null;

});

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
        else if(this.value=="sustraccion_movimiento") {
            $('#valor_1').show();
            $('#valor_2').hide();
            $('#valor_r').hide();
            $('#out').hide();
            $("#label_1").text("C");
            $("#label_2").text("");
            $("#label_r").text("");
        }else if(this.value=="multiplicacionC") {
            $('#valor_1').show();
            $('#valor_2').hide();
            $('#valor_r').hide();
            $('#out').hide();
            $("#label_1").text("C");
            $("#label_2").text("");
            $("#label_r").text("");
        }else if(this.value=="blending") {
            $('#valor_1').show();
            $('#valor_2').hide();
            $('#valor_r').hide();
            $('#out').hide();
            $("#label_1").text("X");
            $("#label_2").text("");
            $("#label_r").text("");
        }     
        else { // adicion,adicion_gris  division, operador_and,operador_or, division_letra(todos los que no reciben parametros, solo imagenes)
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

                	var div = $('<div> </div>', { 
					});

					div.addClass("imagen");

					div.appendTo($('#cuadro'));                	

					var h2 = $('<h2> '+ data.name +'</h2>', { 
                	  id: 'imagen'+i,
					});

                	var img = $('<img >', { 
                	  id: 'imagen'+i,
					});

					div.append(h2)
					img.addClass("remove-img")
					div.append(img)

                    $('#imagen'+i).prop("src", '/static/images/' + data.name);

                    i = i+ 1
                }
            });
        }        
    });

    $('form').on('submit', function(event) {

        event.preventDefault();     

        document.getElementById("file").value = null;

        $.ajax({ 
            url: '/calcular',
            data: { valor_1: $('#valor_1').val(),
                    valor_2: $('#valor_2').val(),
                    valor_r: $('#valor_r').val(),
                    operador: $('#operador').val()
                },
            type: 'POST'
        }).done(function(data) {


        	var div = $('<div> </div>', { 
			});

			div.addClass("imagen");

			div.appendTo($('#cuadro'));                	

        	var h2 = $('<h2> '+ $('#operador').val() +' </h2>', { 
            	  id: 'imagen'+i
				});

        	var img = $('<img >', { 
            	  id: 'imagen'+i
				});

        	div.append(h2)
        	img.addClass("remove-img")
			div.append(img)

            var source = '/static/images/' +data.name,
            timestamp = (new Date()).getTime(),
            newUrl = source + '?_=' + timestamp;
            document.getElementById("imagen"+i).src = newUrl;

            i = i+ 1
            
        }).fail(function() {
            console.log('Failed');
        });        
    });     

});