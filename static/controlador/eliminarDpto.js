function eliminarDpto(id){
     Swal.fire({
          "title": "¿Seguro que quieres eliminar?",
          "icon":"question",
          "showCancelButton":true,
          "cancelButtonText":"No",
          "confirmButtonText":"Si",
          "reverseButtons":true,
          "confirmButtonColor":"red"
      }) 
      .then(function(result){
          if(result.isConfirmed){
               window.location.href="/eliminarDpto/"+id+"/"
          }
      })

}



// <!-- Capturar el id del Departamento que vamos a eliminar en JavaScript -->