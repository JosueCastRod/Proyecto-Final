function eliminarAlumno(IdAlumno){
    if(confirm('¿ Estas seguro de eliminar al Alumno:'+IdAlumno+'?'))
        location.href='/DeleteAlumno/'+IdAlumno;
}
function eliminarBanco(id){
    if(confirm('¿ Estas seguro de eliminar el Banco: '+id))
        location.href='/DeleteBancos/'+id;
}
function eliminarCarrera(id){
    if(confirm('¿ Estas seguro de eliminar la carrera: '+id))
        location.href='/DeleteCarrera/'+id;
}
function eliminarCategoria(id){
    if(confirm('¿ Estas seguro de eliminar la categoria: '+id))
        location.href='/DeleteCategoria/'+id;
}
function eliminarDocente(id){
    if(confirm('¿ Estas seguro de eliminar el Docente: '+id))
        location.href='/DeleteDocente/'+id;
}
function eliminarEdicion(id){
    if(confirm('¿ Estas seguro de eliminar la edicion: '+id))
        location.href='/DeleteEdicion/'+id;
}
function eliminarEquipo(id){
    if(confirm('¿ Estas seguro de eliminar el Equipo: '+id))
        location.href='/DeleteEquipo/'+id;
}
function eliminarProblemaResuelto(id){
    if(confirm('¿ Estas seguro de eliminar el Problema: '+id))
        location.href='/DeleteProblemasResueltos/'+id;
}
function eliminarStaff(id){
    if(confirm('¿ Estas seguro de eliminar el Staff: '+id))
        location.href='/DeleteStaff/'+id;
}
function eliminarTipoUsuario(id){
    if(confirm('¿ Estas seguro de eliminar el TipoUsuario: '+id))
        location.href='/DeleteUsuarios/'+id;
}
//validacion de datos

function ValidarBanco(){
    var cad="";
    if(document.getElementById("Nombre").value.length >150);
    {
        cad+="Nombre del banco con longitud superada";
    }
    if(document.getElementById("Descripcion").value.length >3);
    {
        cad+="Descripcion del banco con longitud superada";
    }
    if(document.getElementById("ColorGlobo").value.length >30);
    {
        cad+="Color del banco con longitud superada";
    }
    if(cad!="")
    {
        alert("Algunos datos no cumplen los requisitos, redireccionando al Banco: "+cad);
        location.href='/Banco';
    }
}

function ValidarAlumnos(){
    var cad="";
    if(document.getElementById("Nombre").value.length >150);
    {
        cad+=" Nombre del alumno con longitud superada.";
    }
    if(document.getElementById("Sexo").value.length >15);
    {
        cad+=" Sexo del alumno con longitud superada.";
    }
    if(document.getElementById("Telefono").value.length >10);
    {
        cad+=" Telefono del Alumno con longitud superada.";
    }
    if(document.getElementById("Email").value.length >150);
    {
        cad+=" Email del Alumno con longitud superada.";
    }
    if(document.getElementById("Contraseña").value.length >15);
    {
        cad+=" Contraseña del Alumno con longitud superada.";
    }
    if(document.getElementById("NumeroControl").value.length >10);
    {
        cad+=" Numero de control del Alumno con longitud superada.";
    }
    if(document.getElementById("Semestre").value.length >1);
    {
        cad+=" Semestre del Alumno con longitud superada.";
    }
    if(document.getElementById("Asesor").value.length >150);
    {
        cad+=" Nombre del asesor del Alumno con longitud superada.";
    }
    if(cad!="")
    {
        alert("Algunos datos no cumplen los requisitos, redireccionando a la consulta de Alumnos: "+cad);
        location.href='/Alumnos';
    }
    alert("Hola "+cad);
}

function ValidarCarrera(){
    var cad="";
    if(document.getElementById("Nombre").value.length >150);
    {
        cad+=" Nombre del carrera con longitud superada.";
    }
    if(document.getElementById("Siglas").value.length >5);
    {
        cad+=" Siglas del Carrera con longitud superada.";
    }
    if(cad!="")
    {
        alert("Algunos datos no cumplen los requisitos, redireccionando a la consulta de Carreras: "+cad);
        location.href='/Carreras';
    }
}