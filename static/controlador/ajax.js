function editarDpto (id, nombre){
     // Mostrar plantilla
     let editaDpto=document.getElementById("formEditarDpto") ;         //Toma el div de (Deptor) en la variable editaDpto
     let htmlInterno="<input type='text' id='nombreDpto' value= '" +nombre+" '>";          //Insertar Html desde Js
     htmlInterno +="<button class='editar' onclick='llamarAjax(" +id +")'>Editar</button> ";        //Se llama la funcion llamarAjax al dar clic
     editaDpto.innerHTML=htmlInterno;
     
}

// Enviar al servidor
// Esperar respuesta y dar mensaje (Ej:Registro actualizado)
function llamarAjax(id){
     let nuevoNombre= document.getElementById("nombreDpto").value;
     let url="http://localhost:8000/editarDpto/";
     let datos={
          'id': id,
          'nuevoNombre' : nuevoNombre
     };

     //Se llama la funcion mensajeAjax
    
     mensajeAjax(url, datos, editarDptoRta);
   
}

//Funcion de respuesta del servidor(callBack)
function editarDptoRta(data){
     console.log(data)    //Provisional
     let editaDpto=document.getElementById("formEditarDpto") ;
     let msj = "<div class='message'>"+ data['mensaje']+"</div>"
     editaDpto.innerHTML += msj;
}

function mensajeAjax(url,datos,callBackFunction) {
     const csrftoken=getCookie('csrftoken');
     fetch(url,{         //Objeto Ajax para comunicacion con el servidor
          method:  'POST',
          credentials: 'same-origin',       //Comunicacion interna  con el mismo servidor
          headers: {
               'Accept' : 'aplication/json',
               'X-Requested-With':'XMLHttpRequest',
               'X-CSRFToken' : csrftoken,
          },
          body: JSON.stringify(datos) //Objeto de datos POST a enviar al servidor
     }) 
          //Traslada los datos de JSON a un objeto JavaScript
     .then(response=>response.json())//Convierte la respuesta JSON en data
     .then(data=>{
          callBackFunction(data)
     })
     //En caso que falle
     .catch((error)=>{
          console.error('Error:', JSON.stringify(error));
     });
}


function getCookie(name){
     let cookieValue= null;
     if(document.cookie && document.cookie !== ""){
          const cookies = document.cookie.split(";");       //Lee el archivo de cookies y las separa en un arreglo
          console.log(cookies)          //Provisional
          //Ciclo para buscar la cookie especifica
          for (let i=0; i< cookies.length; i++){
               const cookie=cookies[i].trim();    //Quita espacio en blanco en los extremos de la cadena
               if(cookie.substring(0,name.length +1)===(name + "=")){
                    cookieValue=decodeURIComponent(cookie.substring(name.length +1));
                    break;
               }
          }
     }
     return cookieValue;
}