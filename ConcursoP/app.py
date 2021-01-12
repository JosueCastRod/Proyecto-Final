from flask import Flask, render_template, abort, request, redirect, url_for
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from modelo.model import db, TipoUsuarios,Carrera,Categoria,Alumno,Docentes,Staf,ProblemasResuelto,Edicion,Equipo,Bancos

app = Flask(__name__)
app.secret_key = 'ConcursoP'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://concurso:hola.123@localhost/ConcursoP'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuración para el manejo de la sesion de los usuarios
loginManager = LoginManager()
loginManager.init_app(app)
loginManager.login_view = "inicio"


@loginManager.user_loader
def load_user(Id):
    return Alumno.query.get(int(Id))
    
    

@app.route('/')
def inicio():
    if current_user.is_authenticated:
        return redirect(url_for('iniciosesion'))
    else:
        return render_template('Index/inicio.html')

@app.route('/iniciar')
def iniciosesion():
    if current_user.IdTipo==1:
        return render_template('Alumnos/registroAlumnos.html')
    else:
        return render_template('Index/inicio.html')

    
    

@app.route('/login',methods=['POST'])
def login():
    u = Alumno()
    u = u.validar(request.form['email'], request.form['password'])
    if u != None:
        login_user(u)
        return redirect(url_for('iniciosesion'))

    d = Docentes()
    d = d.validar(request.form['email'], request.form['password'])
    if d != None:
        login_user(d,d.IdTipo)
        return redirect(url_for('iniciosesion'))

    s = Staf()
    s = s.validar(request.form['email'], request.form['password'])
    if s != None:
        login_user(s)
        return redirect(url_for('iniciosesion'))
    
    return 'Datos incorrectos'

@app.route('/cerrarSesion')
@login_required
def cerrarSesion():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for("inicio"))
    else:
        return render_template('Index/inicio.html')


#Inicio Crud TipoUsuario
@app.route('/Usuarios')
@login_required
def consultaUsuarios():
    u = TipoUsuarios()
    u = u.consultaGeneral()
    return render_template('Usuarios/usuario.html', Usuarios=u)

@app.route('/AddUsuario',methods=['POST'])
@login_required
def guardarUsuarios():
    u = TipoUsuarios()
    u.Alumno  = request.form['tipoUsuario']
    u.Asesor = request.form['tipoUsuario']
    u.Staff = request.form['tipoUsuario']
    u.insertar()
    return redirect(url_for('consultaUsuarios'))

@app.route('/EditUsuario/<int:id>')
@login_required
def consultarUsuario(id):
    u = TipoUsuarios()
    u.IdTipo  = id
    u = u.consultaIndividual()
    return render_template('Usuarios/EditUsuario.html', Usuario=u)

@app.route('/Usuarios/modificar', methods=['POST'])
@login_required
def actualizarUsuario():
    u = TipoUsuarios()
    u.IdTipo     = request.form['IdTipo']
    u.Alumno  = request.form['tipoUsuario']
    u.Asesor = request.form['tipoUsuario']
    u.Staff = request.form['tipoUsuario']
    u.actualizar()
    return redirect(url_for('consultaUsuarios'))

@app.route('/DeleteUsuarios/<int:id>')
@login_required
def eliminarUsuario(id):
    u = TipoUsuarios()
    u.IdTipo = id
    u.eliminar()
    return redirect(url_for('consultaUsuarios'))       
#Fin Crud Usuarios

#Inicio Crud Carreras
@app.route('/Carreras')
@login_required
def consultaCarreras():
    c = Carrera()
    c = c.consultaGeneral()
    return render_template('Carreras/Carrera.html', Carreras=c)

@app.route('/AddCarrera',methods=['POST'])
@login_required
def guardarCarrera():
    c = Carrera()
    c.Nombre  = request.form['Nombre']
    c.Siglas = request.form['Siglas']
    c.insertar()
    return redirect(url_for('consultaCarreras'))

@app.route('/EditCarrera/<int:id>')
@login_required
def consultarCarrera(id):
    c = Carrera()
    c.IdCarrera  = id
    c = c.consultaIndividual()
    return render_template('Carreras/EditCarrera.html', Carrera=c)

@app.route('/Carreras/modificar', methods=['POST'])
@login_required
def actualizarCarrera():
    c = Carrera()
    c.IdCarrera  = request.form['IdCarrera']
    c.Nombre  = request.form['Nombre']
    c.Siglas = request.form['Siglas']
    c.actualizar()
    return redirect(url_for('consultaCarreras'))

@app.route('/DeleteCarrera/<int:id>')
@login_required
def eliminarCarrera(id):
    c = Carrera()
    c.IdCarrera = id
    c.eliminar()
    return redirect(url_for('consultaCarreras'))       
#Fin Crud Carreras

#Inicio Crud Categoria
@app.route('/Categorias')
@login_required
def consultaCategorias():
    c = Categoria()
    c = c.consultaGeneral()
    return render_template('Categorias/Categoria.html', Categorias=c)

@app.route('/AddCategoria',methods=['POST'])
@login_required
def guardarCategoria():
    c = Categoria()
    c.Nombre  = request.form['Nombre']
    c.SemestreLimite = request.form['Semestre']
    c.insertar()
    return redirect(url_for('consultaCategorias'))

@app.route('/EditCategoria/<int:id>')
@login_required
def consultarCategoria(id):
    c = Categoria()
    c.IdCategoria  = id
    c = c.consultaIndividual()
    return render_template('Categorias/EditCategoria.html', Categoria=c)

@app.route('/Categorias/modificar', methods=['POST'])
@login_required
def actualizarCCategoria():
    c = Categoria()
    c.IdCategoria = request.form['IdCategoria']
    c.Nombre  = request.form['Nombre']
    c.SemestreLimite = request.form['Semestre']
    c.actualizar()
    return redirect(url_for('consultaCategorias'))

@app.route('/DeleteCategoria/<int:id>')
@login_required
def eliminarCategoria(id):
    c = Categoria()
    c.IdCategoria = id
    c.eliminar()
    return redirect(url_for('consultaCategorias'))       
#Fin Crud Categorias

#Inicio Crud Equipos
@app.route('/Equipos')
@login_required
def consultaEquipos():
    c = Equipo()
    c = c.consultaGeneral()
    return render_template('Equipos/registrarEquipo.html', Equipos=c)

@app.route('/AddEquipos',methods=['POST'])
@login_required
def guardarEquipo():
    c = Equipo()
    c.Nombre  = request.form['Nombre']
    c.Integrantes = (request.form['Primero'] +" "+ request.form['Segundo'] +" "+ request.form['Tercero'])
    c.Asesor = request.form['Asesor']
    c.IdCategoria = request.form['IdCategoria']
    c.Puntos = request.form['Puntos']
    c.ProblemasResueltos = request.form['Problemas']
    c.insertar()
    return redirect(url_for('consultaEquipos'))

@app.route('/EditEquipo/<int:id>')
@login_required
def consultarEquipo(id):
    c = Equipo()
    c.IdEquipo  = id
    c = c.consultaIndividual()
    return render_template('Equipos/EditEquipo.html', Equipo=c)

@app.route('/Equipos/modificar', methods=['POST'])
@login_required
def actualizarEquipo():
    c = Equipo()
    c.IdEquipo  = request.form['IdEquipo']
    c.Nombre  = request.form['Nombre']
    c.Integrantes = (request.form['Primero'])
    c.Asesor = request.form['Asesor']
    c.IdCategoria = request.form['IdCategoria']
    c.Puntos = request.form['Puntos']
    c.ProblemasResueltos = request.form['Problemas']
    c.actualizar()
    return redirect(url_for('consultaEquipos'))

@app.route('/DeleteEquipo/<int:id>')
@login_required
def eliminarEquipo(id):
    c = Equipo()
    c.IdEquipo = id
    c.eliminar()
    return redirect(url_for('consultaEquipos'))       
#Fin Crud Equipos

#Inicio Crud Alumnos
@app.route('/Alumnos')
@login_required
def consultaAlumnos():
    c = Alumno()
    c = c.consultaGeneral()
    return render_template('Alumnos/registroAlumnos.html', Alumnos=c)

@app.route('/AddAlumno',methods=['POST'])
@login_required
def guardarAlumno():
    c = Alumno()
    c.Nombre  = request.form['Nombre']
    c.Sexo = request.form['Sexo']
    c.Telefono = request.form['Telefono']
    c.Email = request.form['Email']
    c.IdTipo = request.form['IdTipo']
    c.Contraseña = request.form['Contraseña']
    c.NumeroControl = request.form['NumeroControl']
    c.Semestre = request.form['Semestre']
    c.IdCarrera = request.form['IdCarrera']
    c.IdEquipo = request.form['IdEquipo']
    c.NombreAsesor = request.form['NombreAsesor']
    c.insertar()
    return redirect(url_for('consultaAlumnos'))

@app.route('/EditAlumno/<int:id>')
@login_required
def consultarAlumno(id):
    c = Alumno()
    c.IdAlumno  = id
    c = c.consultaIndividual()
    return render_template('Alumnos/EditAlumnos.html', Alumno=c)

@app.route('/Alumnos/modificar', methods=['POST'])
@login_required
def actualizarAlumno():
    c = Alumno()
    c.IdAlumno  = request.form['IdAlumno']
    c.Nombre  = request.form['Nombre']
    c.Sexo = request.form['Sexo']
    c.Telefono = request.form['Telefono']
    c.Email = request.form['Email']
    c.IdTipo = request.form['IdTipo']
    c.Contraseña = request.form['Contraseña']
    c.NumeroControl = request.form['NumeroControl']
    c.Semestre = request.form['Semestre']
    c.IdCarrera = request.form['IdCarrera']
    c.IdEquipo = request.form['IdEquipo']
    c.NombreAsesor = request.form['NombreAsesor']
    c.actualizar()
    return redirect(url_for('consultaAlumnos'))

@app.route('/DeleteAlumno/<int:id>')
@login_required
def eliminarAlumno(id):
    c = Alumno()
    c.IdAlumno = id
    c.eliminar()
    return redirect(url_for('consultaAlumnos'))       
#Fin Crud Alumnos

#Inicio Crud Docentes
@app.route('/Docentes')
@login_required
def consultaDocentes():
    c = Docentes()
    c = c.consultaGeneral()
    return render_template('Docentes/registroDocente.html', Docentes=c)

@app.route('/AddDocente',methods=['POST'])
@login_required
def guardarDocente():
    c = Docentes()
    c.Nombre  = request.form['Nombre']
    c.Sexo = request.form['Sexo']
    c.Telefono = request.form['Telefono']
    c.Email = request.form['Email']
    c.Estatus = request.form['Estatus']
    c.Contraseña = request.form['Contraseña']
    c.IdTipo = request.form['IdTipo']
    c.NumeroDocente = request.form['NumeroDocente']
    c.Escolaridad = request.form['Escolaridad']
    c.Especialidad = request.form['Especialidad']
    c.Cedula = request.form['Cedula']
    c.IdCarrera = request.form['IdCarrera']
    c.insertar()
    return redirect(url_for('consultaDocentes'))

@app.route('/EditDocente/<int:id>')
@login_required
def consultarDocentes(id):
    c = Docentes()
    c.IdDocente  = id
    c = c.consultaIndividual()
    return render_template('Docentes/EditDocente.html', Docentes=c)

@app.route('/Docentes/modificar', methods=['POST'])
@login_required
def actualizarDocentes():
    c = Docentes()
    c.IdDocente  = request.form['IdDocente']
    c.Nombre  = request.form['Nombre']
    c.Sexo = request.form['Sexo']
    c.Telefono = request.form['Telefono']
    c.Email = request.form['Email']
    c.Estatus = request.form['Estatus']
    c.Contraseña = request.form['Contraseña']
    c.IdTipo = request.form['IdTipo']
    c.NumeroDocente = request.form['NumeroDocente']
    c.Escolaridad = request.form['Escolaridad']
    c.Especialidad = request.form['Especialidad']
    c.Cedula = request.form['Cedula']
    c.IdCarrera = request.form['IdCarrera']
    c.actualizar()
    return redirect(url_for('consultaDocentes'))

@app.route('/DeleteDocente/<int:id>')
@login_required
def eliminarDocentes(id):
    c = Docentes()
    c.IdDocente = id
    c.eliminar()
    return redirect(url_for('consultaDocentes'))       
#Fin Crud Docentes

#Inicio Crud Staff
@app.route('/Staff')
@login_required
def consultaStaff():
    c = Staf()
    c = c.consultaGeneral()
    return render_template('Staff/registroStaff.html', Staff=c)

@app.route('/AddStaff',methods=['POST'])
@login_required
def guardarStaff():
    c = Staf()
    c.Nombre  = request.form['Nombre']
    c.Sexo = request.form['Sexo']
    c.Telefono = request.form['Telefono']
    c.Email = request.form['Email']
    c.IdTipo = request.form['IdTipo']
    c.Estatus = request.form['Estatus']
    c.Contraseña = request.form['Contraseña']
    c.insertar()
    return redirect(url_for('consultaStaff'))

@app.route('/EditStaff/<int:id>')
@login_required
def consultarStaff(id):
    c = Staf()
    c.IdStaff  = id
    c = c.consultaIndividual()
    return render_template('Staff/EditStaff.html', Staff=c)

@app.route('/Staff/modificar', methods=['POST'])
@login_required
def actualizarStaff():
    c = Staf()
    c.IdStaff  = request.form['IdStaff']
    c.Nombre  = request.form['Nombre']
    c.Sexo = request.form['Sexo']
    c.Telefono = request.form['Telefono']
    c.Email = request.form['Email']
    c.IdTipo = request.form['IdTipo']
    c.Estatus = request.form['Estatus']
    c.Contraseña = request.form['Contraseña']
    c.actualizar()
    return redirect(url_for('consultaStaff'))

@app.route('/DeleteStaff/<int:id>')
@login_required
def eliminarStaff(id):
    c = Staf()
    c.IdStaff = id
    c.eliminar()
    return redirect(url_for('consultaStaff'))       
#Fin Crud Staff

#Inicio Crud ProblemasResueltos
@app.route('/ProblemasResueltos')
@login_required
def consultaProblemasResueltos():
    c = ProblemasResuelto()
    c = c.consultaGeneral()
    return render_template('ProblemasResueltos/registroProblemas.html', ProblemasResueltos=c)

@app.route('/AddProblemasResueltos',methods=['POST'])
@login_required
def guardarProblemasResueltos():
    c = ProblemasResuelto()
    c.Tiempo  = request.form['Tiempo']
    c.insertar()
    return redirect(url_for('consultaProblemasResueltos'))

@app.route('/EditProblemasResueltos/<int:id>')
@login_required
def consultarProblemasResueltos(id):
    c = ProblemasResuelto()
    c.IdProblema  = id
    c = c.consultaIndividual()
    return render_template('ProblemasResueltos/EditProblemas.html', ProblemaResuelto=c)

@app.route('/ProblemasResueltos/modificar', methods=['POST'])
@login_required
def actualizarProblemasResueltos():
    c = ProblemasResuelto()
    c.IdProblema  = request.form['IdProblema']
    c.Tiempo  = request.form['Tiempo']
    c.actualizar()
    return redirect(url_for('consultaProblemasResueltos'))

@app.route('/DeleteProblemasResueltos/<int:id>')
@login_required
def eliminarProblemasResueltos(id):
    c = ProblemasResuelto()
    c.IdProblema = id
    c.eliminar()
    return redirect(url_for('consultaProblemasResueltos'))       
#Fin Crud ProblemasResueltos

#Inicio Crud Edicion
@app.route('/Edicion')
@login_required
def consultaEdicion():
    c = Edicion()
    c = c.consultaGeneral()
    return render_template('Ediciones/edicion.html', Ediciones=c)

@app.route('/AddEdicion',methods=['POST'])
@login_required
def guardarEdicion():
    c = Edicion()
    c.Nombre  = request.form['Nombre']
    c.FechaRegistro = request.form['FechaRegistro']
    c.FechaEvento = request.form['FechaEvento']
    c.insertar()
    return redirect(url_for('consultaEdicion'))

@app.route('/EditEdicion/<int:id>')
@login_required
def consultarEdicion(id):
    c = Edicion()
    c.IdEdicion  = id
    c = c.consultaIndividual()
    return render_template('Ediciones/EditEdicion.html', Edicion=c)

@app.route('/Edicion/modificar', methods=['POST'])
@login_required
def actualizarEdicion():
    c = Edicion()
    c.IdEdicion  = request.form['IdEdicion']
    c.Nombre  = request.form['Nombre']
    c.FechaRegistro = request.form['FechaRegistro']
    c.FechaEvento = request.form['FechaEvento']
    c.actualizar()
    return redirect(url_for('consultaEdicion'))

@app.route('/DeleteEdicion/<int:id>')
@login_required
def eliminarEdicion(id):
    c = Edicion()
    c.IdEdicion = id
    c.eliminar()
    return redirect(url_for('consultaEdicion'))       
#Fin Crud Edicion

#Inicio Crud Banco
@app.route('/Banco')
@login_required
def consultaBanco():
    c = Bancos()
    c = c.consultaGeneral()
    return render_template('Banco/banco.html', Bancos=c)

@app.route('/AddBancos',methods=['POST'])
@login_required
def guardarBancos():
    c = Bancos()
    c.Nombre  = request.form['Nombre']
    c.Puntos = request.form['Puntos']
    c.Tiempo = request.form['Tiempo']
    c.Descripcion = request.form['Descripcion']
    c.ColorGlobo = request.form['ColorGlobo']
    c.insertar()
    return redirect(url_for('consultaBanco'))

@app.route('/EditBancos/<int:id>')
@login_required
def consultarBancos(id):
    c = Bancos()
    c.IdBanco  = id
    c = c.consultaIndividual()
    return render_template('Banco/EditBanco.html', Banco=c)

@app.route('/Bancos/modificar', methods=['POST'])
@login_required
def actualizarBancos():
    c = Bancos()
    c.IdBanco  = request.form['IdBanco']
    c.Nombre  = request.form['Nombre']
    c.Puntos = request.form['Puntos']
    c.Tiempo = request.form['Tiempo']
    c.Descripcion = request.form['Descripcion']
    c.ColorGlobo = request.form['ColorGlobo']
    c.actualizar()
    return redirect(url_for('consultaBanco'))

@app.route('/DeleteBancos/<int:id>')
@login_required
def eliminarBancos(id):
    c = Bancos()
    c.IdBanco = id
    c.eliminar()
    return redirect(url_for('consultaBanco'))       
#Fin Crud Banco

@app.errorhandler(404)
def error_404(e):
    return redirect(url_for('inicio')),404

@app.errorhandler(500)
def error_500(e):
    return redirect(url_for('inicio')),500

@app.errorhandler(505)
def error_505(e):
    return redirect(url_for('inicio')),505


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
