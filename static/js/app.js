$(document).ready(function(){
    $("#regprove").validate({
        errorClass: 'is-invalid',
        rules:{
            idprove:{
                required: true,
                minlength:3,
                maxlength:3,
            },
            nomprove:{
                required:true,
                maxlength:60,
                minlength:2

            },
            rutprove:{
                required:true
                
            },
            contactoprove:{
                required:true
                
            },
            fonoprove:{
                required:true
                
            },
            direcprove:{
                required:true
                
            },
            rubroprove:{
                required:true

            }
        },
        messages:{
            idprove:{
                required:"Este campo no puede estar vacío",
                minlength:"Debe tener un mínimo de 3 dígitos",
                maxlength:"Debe tener un máximo de 3 dígitos"
            },
            nomprove:{
                required:"Este campo no puede estar vacío",
                maxlength:"Máximo 60 carácteres",
                minlength:"Mínimo 2 carácter"
            },
            rutprove:{
                required:"Este campo no puede estar vacío",
                
            },
            contactoprove:{
                required:"Este campo no puede estar vacío",
                
            },
            fonoprove:{
                required:"Este campo no puede estar vacío",
                
            },
            direcprove:{
                required:"Este campo no puede estar vacío",
                
            },
            rubroprove:{
                required:"Este campo no puede estar vacío",

            }


        }
    }),
    $("#regcli").validate({
        errorClass: 'is-invalid',
        rules:{
            rutcli:{
                required: true 
            },
            nomcli:{
                required: true,
                maxlength: 60,
                minlength: 2
            },
            apecli:{
                required: true,
                maxlength: 60,
                minlength: 2
            },
            direcli:{
                required:true,
                maxlength:60
            },
            fonocli:{
                required:true,
                minlength:8
            },
            correocli:{
                email:true
            }
        },
        messages:{
            rutcli:{
                required: "Este campo no puede estar en blanco" 
            },
            nomcli:{
                required: "Este campo no puede estar en blanco",
                maxlength: "Máximo 60 carácteres",
                minlength: "Mínimo 2 carácteres"
            },
            apecli:{
                required: "Este campo no puede estar en blanco",
                maxlength: "Máximo 60 carácteres",
                minlength: "Mínimo 2 carácteres"
            },
            direcli:{
                required:"Este campo no puede estar en blanco",
                maxlength:"Máximo 60 carácteres"
            },
            fonocli:{
                required:"Este campo no puede estar en blanco",
                minlength:"Mínimo 8 dígitos"
            },
            correocli:{
                email:"Ingrese un formato de mail correcto"
            }
        }
    }),
    $("#regprodu").validate({
        errorClass:'is-invalid',
        rules:{
            descprodu:{
                required:true,
                maxlength:50
            },
            compraprodu:{
                required:true,
                minlength:1
            },
            ventaprodu:{
                required: true,
                minlength:1
            },
            marcaprodu:{
                required:true,
                maxlength:50
            },
            codfamprodu:{
                required:true,
                minlength:3,
                maxlength:3
            },
            fecprodu:{
                required:true,
                minlength:8,
                maxlength:8
            }
        },
        messages:{
            descprodu:{
                required:"Este campo no puede estar en blanco",
                maxlength:"Máximo 50 carácteres"
            },
            compraprodu:{
                required:"Este campo no puede estar en blanco",
                minlength:"Mínimo 1 carácter"
            },
            ventaprodu:{
                required: "Este campo no puede estar en blanco",
                minlength:"Mínimo 1 carácter"
            },
            marcaprodu:{
                required:"Este campo no puede estar en blanco",
                maxlength:"Máximo 50 carácteres"
            },
            codfamprodu:{
                required:"Este campo no puede estar en blanco",
                minlength:"Mínimo 3 carácteres",
                maxlength:"Máximo 3 carácteres"
            },
            fecprodu:{
                required:"Este campo no puede estar en blanco",
                minlength:"Mínimo 8 dígitos",
                maxlength:"Máximo 8 dígitos"
            }
        }
    }),
    $( document ).ready(function() {
        
        var now = new Date();
    
        var day = ("0" + now.getDate()).slice(-2);
        var month = ("0" + (now.getMonth() + 1)).slice(-2);
    
        var today = now.getFullYear()+"-"+(month)+"-"+(day) ;
        $("#fecventa").val(today);
        $("#fecpedido").val(today);
    });
    $('#ventaacredi2').click(function(){
        $('#bloqueabono').hide();
        $('#bloqueboletacredi').hide();

    });
    $('#ventaacredi1').click(function(){
        $('#bloqueabono').show();
        $('#bloqueboletacredi').show();
    });
});